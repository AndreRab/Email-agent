from dotenv import load_dotenv
import os

load_dotenv()

BASE_MODEL_URL = os.getenv("BASE_MODEL_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_API_KEY = os.getenv("MODEL_API_KEY")