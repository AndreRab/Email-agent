from dotenv import load_dotenv
import os

load_dotenv()

APPLICATION_KEY = os.getenv("APPLICATION_KEY")
CLIENT_SECRETS_FILE = os.getenv("CLIENT_SECRETS_FILE")