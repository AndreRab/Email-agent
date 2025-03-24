import telebot 
import requests
import re
from keys import *
from constans import *

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

COMMANDS = [ telebot.types.BotCommand(name, description) for name, description in COMMAND_DESCRIPTION.items() ]

bot.set_my_commands(COMMANDS)

@bot.message_handler(commands=[HELP_COMMAND])
def show_help(message):
    help_text = HELP_TEXT
    for command in COMMANDS:
        help_text += f"/{command.command} - {command.description}\n"
    bot.reply_to(message, help_text)


@bot.message_handler(commands=[START_COMMAND, LOG_IN_COMMAND])
def send_login_button(message):
    chat_id = message.chat.id
    login_url = f"{GMAIL_API_URL}{LOGIN_PATH}{chat_id}"  

    bot.send_message(chat_id, LOG_IN_TEXT + login_url)

@bot.message_handler(commands=[UNREAD_COMMAND])
def check_unread_mails(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, LOADING_TEXT)
    request_url = f"{GMAIL_API_DOCKER_URL}{UNREAD_PATH}{chat_id}"
    response = requests.get(request_url)

    if response.status_code == 401:
        bot.send_message(chat_id, NOT_AUTHORIZED_TEXT)
        return
    
    emails = response.json()
    show_emails(emails, chat_id)

@bot.message_handler(commands = [SET_UNREAD_TO_READ_COMMAND])
def get_emails_from_user(message):
    chat_id = message.chat.id
    request_url = f"{GMAIL_API_DOCKER_URL}{MARK_AS_READ_PATH}{chat_id}"
    bot.send_message(chat_id, LOADING_TEXT)
    response = requests.get(request_url)
    if response.status_code == 401:
        bot.send_message(chat_id, NOT_AUTHORIZED_TEXT)
    elif response.status_code == 200:
        bot.send_message(chat_id, response.json().get('message', ERROR_MESSAGE_TEXT))
    else:
        bot.send_message(chat_id, ERROR_MESSAGE_TEXT)

@bot.message_handler(commands = [AGENT_COMMAND])
def invoke_agent(message):
    chat_id = message.chat.id
    text = message.text
    try:
        prompt = text[(len(AGENT_COMMAND) + 2):]
        if prompt.strip() == "":
            prompt = STANDART_AGENT_PROMPT
    except(IndexError):
        bot.send_message(chat_id, 'Error with the formating')
        return
    bot.send_message(chat_id, LOADING_TEXT)
    request_url = f"{AGENT_API_DOCKER_URL}{AGENT_REQUEST_PATH}{prompt}/{chat_id}"
    response = requests.get(request_url)
    if response.status_code == 401:
        bot.send_message(chat_id, NOT_AUTHORIZED_TEXT)
    elif response.status_code == 200:
        bot.send_message(chat_id, response.json())
    else:
        bot.send_message(chat_id, ERROR_MESSAGE_TEXT)

@bot.message_handler(commands = [USER_COMMAND])
def get_user(message):
    bot.send_message(message.chat.id, SENDER_EMAIL_TEXT)
    bot.register_next_step_handler(message, show_emails_from_sender)

def show_emails_from_sender(message):
    email = message.text.strip()
    chat_id = message.chat.id
    if re.match(EMAIL_REGEX, email):
        show_emails_by_user(email, chat_id, 10)
    else:
        bot.send_message(chat_id, WRONG_EMAIL_FORMAT_TEXT)
        bot.register_next_step_handler(message, show_emails_from_sender)  

def show_emails_by_user(user_email, chat_id, emails_number):
    bot.send_message(chat_id, LOADING_TEXT)
    request_url = f"{GMAIL_API_DOCKER_URL}{SENDER_PATH}{chat_id}/{user_email}/{emails_number}"
    response = requests.get(request_url)

    if response.status_code == 401:
        bot.send_message(chat_id, NOT_AUTHORIZED_TEXT)
        return
    
    emails = response.json()
    show_emails(emails, chat_id)


def show_emails(emails, chat_id):
    if not emails:
        bot.send_message(chat_id, NO_UNREAD_MAILS_TEXT)
    else:
        for email in emails:
            sender = email.get("sender", DEFAULT_SENDER_TEXT)
            subject = email.get("subject", DEFULT_SUBJECT_TEXT)
            snippet = email.get("snippet", DEFAULT_SNIPPET_TEXT)
            bot.send_message(chat_id, BOT_MESSAGE_TEMPLATE(sender, subject, snippet), parse_mode="Markdown")



if __name__ == "__main__":
    bot.polling(none_stop=True)
    