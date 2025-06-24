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

from pymongo import MongoClient
from .info import DATABASE_URI

dbclient = MongoClient(DATABASE_URI)
db = dbclient["Auto-Delete"]
col = db["DATA"]
col.create_index("time")

def save_message(message, expire_at):
    data = {
        "chat_id": message.chat.id,
        "message_id": message.id,
        "time": expire_at
    }
    col.insert_one(data)

def get_all_data(current_time):
    return list(col.find({"time": {"$lte": current_time}}))

def delete_all_data(records):
    for data in records:
        col.delete_one({"_id": data["_id"]})
