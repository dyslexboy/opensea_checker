import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API keys using os.getenv()
os_api_key = os.getenv("API_KEY_OPENSEA")
os_api_version = os.getenv("API_PATH_OPENSEA")
