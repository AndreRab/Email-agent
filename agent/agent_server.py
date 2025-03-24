from flask import Flask, jsonify 
from constants import *  
from agent import Agent
from keys import *
import requests

app = Flask(__name__)
agent = Agent(BASE_MODEL_URL, MODEL_NAME, MODEL_API_KEY, SYSTEM_PROMPT_PATH)

def compose_emails(emails):
    result = []
    for email in emails:
        sender = email.get("sender", DEFAULT_SENDER_TEXT)
        subject = email.get("subject", DEFULT_SUBJECT_TEXT)
        snippet = email.get("snippet", DEFAULT_SNIPPET_TEXT)
        result.append(BOT_MESSAGE_TEMPLATE(sender, subject, snippet))
    return result

def get_messages_from_sender(email, chat_id):
    request_url = f"{GMAIL_API_DOCKER_URL}{SENDER_PATH}{chat_id}/{email}/{10}"
    response = requests.get(request_url)  
    emails = response.json()
    if response.status_code != 200 or not response.content.strip():
        return {}
    return compose_emails(emails)

def get_unread(chat_id):
    request_url = f"{GMAIL_API_DOCKER_URL}{UNREAD_PATH}{chat_id}"
    response = requests.get(request_url)
    if response.status_code != 200 or not response.content.strip():
        return {}
    return response.json()  

@app.route(AGENT_REQUEST_PATH)
def agent_request(prompt, chat_id):
    available_actions = {
        'get_messages_from_sender': get_messages_from_sender,
        'get_unread': get_unread,
        'final_answer': final_answer
    }
    response = agent(prompt, available_actions, default_action, chat_id=chat_id, debug=True)
    return jsonify(response)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 6000)