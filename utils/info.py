import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# Helper to parse space-separated integers from environment
def parse_int_list(key, default=''):
    return [int(i) for i in os.environ.get(key, default).split() if i.strip().isdigit()]

# Load critical config values
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SESSION = os.environ.get("SESSION", "")
TIME = int(os.environ.get("TIME", "10"))  # default to 10 seconds

# Lists of chat/user IDs
CHATS = parse_int_list("CHATS", "-1001896199579 -1002034897292 -1002182767754")
WHITE_LIST = parse_int_list("WHITE_LIST", "1739381637")
BLACK_LIST = parse_int_list("BLACK_LIST", "")

# Database
DATABASE_URI = os.environ.get("DATABASE_URI", "")
PORT = os.environ.get("PORT", "8080")

# Validate required variables
if not all([API_ID, API_HASH, SESSION, DATABASE_URI]) or not CHATS:
    raise ValueError("Missing required environment variables: API_ID, API_HASH, SESSION, DATABASE_URI, CHATS")
