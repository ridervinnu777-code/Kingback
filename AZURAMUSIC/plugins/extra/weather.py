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
from AZURAMUSIC import app


@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="𝐇ᴇʀᴇ'ꜱ ᴛʜᴇ 𝐖ᴇᴀᴛʜᴇʀ ꜰᴏʀ 𝐘ᴏᴜʀ 𝐋ᴏᴄᴀᴛɪᴏɴ")
    except IndexError:
        # User didn't provide a location
        message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐋ᴏᴄᴀᴛɪᴏɴ. 𝐔ꜱᴇ /weather 𝐍𝐄𝐖 𝐘𝐎𝐑𝐊")
