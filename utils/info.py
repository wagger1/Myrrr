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

API_ID = int(os.environ.get("API_ID", "25578852"))
API_HASH = os.environ.get("API_HASH", "1c8e30eae03f9600dfdee4408db4811a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5937008191:AAG4vWohsfxoiynxQKhHmwRganDyS90toD8")
SESSION = os.environ.get("SESSION", "BQG1DzwAcBDYic6Ml-7pSmXTigL26hVY8m-ZZdRjxMda9wLFc6BJy0wONQAzwgWnZ3T5OGIN_JpwDvKdourn8yRVmETzuHXow5wnh_rCaDoI4rBT2Vp5Tb3Tt48bpkae6ftDYCWlCz7eDg8akhf8XMB0MG_ckzBxEGtU11QUucWYBTxkhvIHAJMDkyn8APSCh9D8T4ekvyTY1yPEDTdlK2YO-i2hOKeRWr5gd8kTBE-19J8UAgSGoNAnHebFYFDl9pyBrBUUtFWQbSODgKitcAo-W5Znh2Lh0KSG9cJLpIqQMZfWoW-hmJpMmxTA7aPhXrj-Y48Y14mIqS6tJyD5XzT4Y26nIwAAAAFRWb3RAA")
TIME = int(os.environ.get("TIME", "10"))  # default to 10 seconds if not set
CHATS = parse_int_list("CHATS", "-1001896199579 -1002034897292 -1002182767754")
WHITE_LIST = parse_int_list("WHITE_LIST", "1739381637")
BLACK_LIST = parse_int_list("BLACK_LIST")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://HALLOO:HALLOO@cluster0.0bubp1j.mongodb.net/?retryWrites=true&w=majority")
PORT = os.environ.get("PORT", "8080")

# Validate required variables
if not all([API_ID, API_HASH, SESSION, DATABASE_URI]) or not CHATS:
    raise ValueError("Missing required environment variables: API_ID, API_HASH, SESSION, DATABASE_URI, CHATS")
