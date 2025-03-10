from flask import Flask, session, redirect, request, jsonify
from keys import APPLICATION_KEY, CLIENT_SECRETS_FILE
from constants import *
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import json

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = APPLICATION_KEY

users_tokens = {}

MAX_RETRIES = 10

@app.route(LOGIN_PATH)
def login(chat_id):
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    auth_url, state = flow.authorization_url(prompt="consent")
    session["state"] = state
    session['chat_id'] = chat_id
    return redirect(auth_url)

@app.route(REDIRECT_PATH)
def callback():
    chat_id = session.get('chat_id')
    if not chat_id:
        return ERROR_MESSAGE_MISSING_ID
    
    state = session.get("state")
    received_state = request.args.get('state')
    if received_state != state:
        return ERROR_MESSAGE_INVALID_STATE
    
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, redirect_uri=REDIRECT_URI)
    flow.fetch_token(authorization_response=request.url)

    users_tokens[chat_id] = flow.credentials.to_json()
    return SUCCESS_LOG_IN_MESSAGE

@app.route(UNREAD_EMAILS_PATH)
def get_unread_emails(chat_id):
    return get_emails(chat_id, EMAIL_UNREAD_QUERY, MAX_EMAIL_UNREAD_LENGTH)

@app.route(SENDER_EMAILS_PATH)
def get_last_emails_from_sender(chat_id, sender_email, emails_number):
    query = f'from:{sender_email}'
    return get_emails(chat_id, query, emails_number) 

@app.route(MARK_AS_READ_PATH)
def mark_all_as_read(chat_id):
    if chat_id not in users_tokens:
        return not_register_response()
    
    creds = Credentials.from_authorized_user_info(json.loads(users_tokens[chat_id]))
    service = build("gmail", "v1", credentials=creds)

    messages_finder = service.users().messages()
    unread_messages = messages_finder.list(
        userId="me", 
        q=EMAIL_UNREAD_QUERY, 
        maxResults=MAX_EMAIL_UNREAD_LENGTH
    ).execute()
    
    messages = unread_messages.get("messages", [])
    for message in messages:
        service.users().messages().modify(
            userId="me", 
            id=message["id"], 
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

    return success_read_reponse()


def get_emails(chat_id, query, maxResults):
    if chat_id not in users_tokens:
        return not_register_response()
    
    creds = Credentials.from_authorized_user_info(json.loads(users_tokens[chat_id]))
    service = build("gmail", "v1", credentials=creds)

    messages_finder = service.users().messages()
    unread_messages = messages_finder.list(
        userId="me", 
        q=query, 
        maxResults=maxResults
    ).execute()
    
    messages = unread_messages.get("messages", [])

    email_list = []

    for message in messages:
        msg = messages_finder.get(userId="me", id=message["id"], format="full").execute()
        headers = msg['payload']['headers']

        sender = next((h['value'] for h in headers if h['name'].lower() == 'from'), 'Unknown')
        subject = next((h["value"] for h in headers if h["name"].lower() == "subject"), "No subject")
        snippet = msg["snippet"]

        email_list.append(
            {
                'sender': sender,
                'subject': subject, 
                'snippet': snippet
            }
        )

    return jsonify(email_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
