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

import asyncio
from time import time
from collections import defaultdict
from .info import *
from .database import get_all_data, delete_all_data
from pyrogram import Client
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AutoDelete")

bot = Client("auto-delete-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def check_up(bot):
    now = int(time())
    due_messages = get_all_data(now)

    grouped = defaultdict(list)
    for msg in due_messages:
        grouped[msg["chat_id"]].append((msg["message_id"], msg["_id"]))

    for chat_id, messages in grouped.items():
        for i in range(0, len(messages), 100):
            batch = messages[i:i + 100]
            message_ids = [m[0] for m in batch]
            try:
                await bot.delete_messages(chat_id=chat_id, message_ids=message_ids)
            except Exception as e:
                logger.warning(f"Failed to delete messages in chat {chat_id}: {e}")

    delete_all_data(due_messages)

async def run_check_up():
    async with bot:
        while True:
            await check_up(bot)
            await asyncio.sleep(10)  # Every 10 seconds

if __name__ == "__main__":
    asyncio.run(run_check_up())
