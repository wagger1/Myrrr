#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

def parse_int_list(key):
    return [int(i) for i in os.environ.get(key, '').split() if i.strip().isdigit()]

API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
SESSION = os.environ.get("SESSION", "")
TIME = int(os.environ.get("TIME", "10"))  # default to 10 seconds if not set
CHATS = parse_int_list("CHATS")
WHITE_LIST = parse_int_list("WHITE_LIST")
BLACK_LIST = parse_int_list("BLACK_LIST")
DATABASE_URI = os.environ.get("DATABASE_URI", "")
PORT = os.environ.get("PORT", "8080")

# Validate required variables
if not all([API_ID, API_HASH, SESSION, DATABASE_URI]) or not CHATS:
    raise ValueError("Missing required environment variables: API_ID, API_HASH, SESSION, DATABASE_URI, CHATS")
