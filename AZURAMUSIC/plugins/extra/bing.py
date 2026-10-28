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
from AZURAMUSIC import app 
import requests as r
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import filters 

API_URL = "https://sugoi-api.vercel.app/search"

@app.on_message(filters.command("bingsearch"))
async def bing_search(michiko, message):
    try:
        if len(message.command) == 1:
            await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐊ᴇʏᴡᴏʀᴅ ᴛᴏ 𝐒ᴇᴀʀᴄʜ.")
            return

        keyword = " ".join(
            message.command[1:]
        )  # Assuming the keyword is passed as arguments
        params = {"keyword": keyword}
        response = r.get(API_URL, params=params)

        if response.status_code == 200:
            results = response.json()
            if not results:
                await message.reply_text("𝐍ᴏ 𝐑ᴇꜱᴜʟᴛꜱ 𝐅ᴏᴜɴᴅ.")
            else:
                message_text = ""
                for result in results[:7]:
                    title = result.get("\x74\x69\x74\x6C\x65", "")
                    link = result.get("\x6C\x69\x6E\x6B", "")
                    message_text += f"{title}\n{link}\n\n"
                await message.reply_text(message_text.strip())
        else:
            await message.reply_text("𝐒ᴏʀʀʏ, 𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ᴇɴᴛ 𝐖ʀᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ 𝐒ᴇᴀʀᴄʜ.")
    except Exception as e:
        await message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
