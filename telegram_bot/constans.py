GMAIL_API_URL = "http://localhost:5000"
GMAIL_API_DOCKER_URL = "http://gmail_service:5000"
# GMAIL_API_DOCKER_URL = GMAIL_API_URL
AGENT_API_URL = "http://localhost:6000"
AGENT_API_DOCKER_URL = AGENT_API_URL
AGENT_API_DOCKER_URL = "http://agent:6000"
LOGIN_PATH = "/oauth/login/"
UNREAD_PATH = '/emails/'
SENDER_PATH = "/emails/from/"
MARK_AS_READ_PATH = "/emails/unread/True/"
AGENT_REQUEST_PATH = '/agent/'

START_COMMAND = 'start' 
HELP_COMMAND = 'help' 
LOG_IN_COMMAND = 'login' 
UNREAD_COMMAND = 'unread'
USER_COMMAND = 'find_user_emails'
SET_UNREAD_TO_READ_COMMAND = 'set_read'
AGENT_COMMAND = 'agent_invoke'

COMMAND_DESCRIPTION = {
    HELP_COMMAND: "Show available commands",
    LOG_IN_COMMAND: "Login to your gmail",
    UNREAD_COMMAND: "Check unread messages",
    USER_COMMAND: "Check last 10 emails from specific user",
    SET_UNREAD_TO_READ_COMMAND: "Set all unread messages as read one",
    AGENT_COMMAND: 'Ask agent to analise your emails'
}

HELP_TEXT = "Available commands:\n"
LOG_IN_TEXT = "🔗 Now you can go to login url: "
NOT_AUTHORIZED_TEXT = "⚠️ You are not authorized. Use /login first."
NO_UNREAD_MAILS_TEXT = "📭 No unread emails."
ERROR_MESSAGE_TEXT = "⚠️ Something went wrong"

DEFAULT_SENDER_TEXT = "Unknown Sender"
DEFULT_SUBJECT_TEXT = "No Subject"
DEFAULT_SNIPPET_TEXT = "No preview available"
LOADING_TEXT = "⏳ Wait a second"

BOT_MESSAGE_TEMPLATE = lambda sender, subject, snippet: f"📩 *New Email*\n👤 *From:* {sender}\n✉️ *Subject:* {subject}\n🔍 *Preview:* {snippet[:200]}"

EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
SENDER_EMAIL_TEXT = "📧 Please enter sender email:"
WRONG_EMAIL_FORMAT_TEXT = "⚠️ Invalid email format. Please try again:"

STANDART_AGENT_PROMPT = "Tell me about my last email's"