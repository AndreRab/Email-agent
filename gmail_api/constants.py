from flask import jsonify

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.readonly"
]

REDIRECT_URI = "http://localhost:1000/oauth/callback"

LOGIN_PATH = "/oauth/login/<chat_id>"
REDIRECT_PATH = "/oauth/callback"

ERROR_MESSAGE_MISSING_ID = "❌ Error: Missing chat ID."
ERROR_MESSAGE_INVALID_STATE = "❌ Error: Invalid state parameter. Possible CSRF attack."
SUCCESS_LOG_IN_MESSAGE = "✅ Authorization successful! You can now use the bot."

UNREAD_EMAILS_PATH = "/emails/<chat_id>"
SENDER_EMAILS_PATH = "/emails/from/<chat_id>/<sender_email>/<emails_number>"
MARK_AS_READ_PATH = "/emails/unread/True/<chat_id>"

EMAIL_UNREAD_QUERY = 'is:unread in:inbox -category:promotions -category:social'
MAX_EMAIL_UNREAD_LENGTH = 10

def not_register_response():
    return jsonify({"error": "Log-in first"}), 401

def success_read_reponse():
    return jsonify({"message": "All unread emails marked as read"}), 200