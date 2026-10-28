# -----------------------------------------------
# 🔴 Azura ✘ Music Project
# 🔷️ Developed & Maintained by: 𝐌ʀ 𝐕ɪɴɴᴜ
# 📅 Copyright © 2026 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# Commercial use, redistribution, or modification of this source
# without prior written permission from the author is prohibited.
#
# ❤️ Made with dedication & love by 𝐌ʀ 𝐕ɪɴɴᴜ
# -----------------------------------------------
from pyrogram import Client, filters
from pyrogram.types import Message
from pymongo import MongoClient
import re
from AZURAMUSIC import app as AZURA


mongo_url_pattern = re.compile(r'mongodb(?:\+srv)?:\/\/[^\s]+')


@AZURA.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply("𝐏ʟᴇᴀꜱᴇ 𝐄ɴᴛᴇʀ 𝐘ᴏᴜʀ 𝐌ᴏɴɢᴏᴅʙ 𝐔𝐑𝐋 𝐀ꜰᴛᴇʀ ᴛʜᴇ 𝐂ᴏᴍᴍᴀɴᴅ. 𝐄xᴀᴍᴘʟᴇ: /mongochk 𝐘ᴏᴜʀ_𝐌ᴏɴɢᴏᴅʙ_𝐔𝐑𝐋")
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗨𝗥𝗟 𝗶𝘀 𝘃𝗮𝗹𝗶𝗱 𝗮𝗻𝗱 𝗰𝗼𝗻𝗻𝗲𝗰𝘁𝗶𝗼𝗻 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹✅")
        except Exception as e:
            await message.reply(f"𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐂ᴏɴɴᴇᴄᴛ ᴛᴏ 𝐌ᴏɴɢᴏᴅʙ: {e}")
    else:
        await message.reply("𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗠𝗼𝗻𝗴𝗼𝗗𝗕 𝗨𝗥𝗟 𝗳𝗼𝗿𝗺𝗮𝘁💔")
