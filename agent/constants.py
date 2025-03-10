GMAIL_API_URL = "http://localhost:5000"
GMAIL_API_DOCKER_URL = "http://gmail_service:5000"
# GMAIL_API_DOCKER_URL = GMAIL_API_URL

REGEX_FOR_ACTION = r'"action"\s*:\s*"([^"]+)"'
REGEX_FOR_PARAMETERS = r'\"action_input\"\s*:\s*({[\s\S]*?})'

SYSTEM_PROMPT_PATH = "system_prompt.txt"
AGENT_REQUEST_PATH = '/agent/<prompt>/<chat_id>'
UNREAD_PATH = '/emails/'
SENDER_PATH = "/emails/from/"

DEFAULT_SENDER_TEXT = "Unknown Sender"
DEFULT_SUBJECT_TEXT = "No Subject"
DEFAULT_SNIPPET_TEXT = "No preview available"

BOT_MESSAGE_TEMPLATE = lambda sender, subject, snippet: f"📩 *New Email*\n👤 *From:* {sender}\n✉️ *Subject:* {subject}\n🔍 *Preview:* {snippet[:200]}"

final_answer = lambda answer: answer
default_action = lambda : 'something went wrong, format your action properly'
