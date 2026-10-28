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
import requests
import random
from AZURAMUSIC import app

# Truth or Dare API URLs
truth_api_url = "https://api.truthordarebot.xyz/v1/truth"
dare_api_url = "https://api.truthordarebot.xyz/v1/dare"


@app.on_message(filters.command("truth"))
def get_truth(client, message):
    try:
        # Make a GET request to the Truth API
        response = requests.get(truth_api_url)
        if response.status_code == 200:
            truth_question = response.json()["question"]
            message.reply_text(f"𝐓ʀᴜᴛʜ 𝐐ᴜᴇꜱᴛɪᴏɴ:\n\n{truth_question}")
        else:
            message.reply_text("𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐅ᴇᴛᴄʜ ᴀ 𝐓ʀᴜᴛʜ 𝐐ᴜᴇꜱᴛɪᴏɴ. 𝐏ʟᴇᴀꜱᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")
    except Exception as e:
        message.reply_text("𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ 𝐖ʜɪʟᴇ 𝐅ᴇᴛᴄʜɪɴɢ ᴀ 𝐓ʀᴜᴛʜ 𝐐ᴜᴇꜱᴛɪᴏɴ. 𝐏ʟᴇᴀꜱᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")

@app.on_message(filters.command("dare"))
def get_dare(client, message):
    try:
        # Make a GET request to the Dare API
        response = requests.get(dare_api_url)
        if response.status_code == 200:
            dare_question = response.json()["question"]
            message.reply_text(f"𝐃ᴀʀᴇ 𝐐ᴜᴇꜱᴛɪᴏɴ:\n\n{dare_question}")
        else:
            message.reply_text("𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐅ᴇᴛᴄʜ ᴀ 𝐃ᴀʀᴇ 𝐐ᴜᴇꜱᴛɪᴏɴ. 𝐏ʟᴇᴀꜱᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")
    except Exception as e:
        message.reply_text("𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ 𝐖ʜɪʟᴇ 𝐅ᴇᴛᴄʜɪɴɢ ᴀ 𝐃ᴀʀᴇ 𝐐ᴜᴇꜱᴛɪᴏɴ. 𝐏ʟᴇᴀꜱᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")
