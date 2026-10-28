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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from AZURAMUSIC import app


def get_pypi_info(package_name):
    try:
        
        api_url = f"https://pypi.org/pypi/{package_name}/json"
        
        # Sending a request to the PyPI API
        response = requests.get(api_url)
        
        # Extracting information from the API response
        pypi_info = response.json()
        
        return pypi_info
    
    except Exception as e:
        print(f"Error fetching PyPI information: {e}")
        return None

@app.on_message(filters.command("pypi", prefixes="/"))
def pypi_info_command(client, message):
    try:
       
        package_name = message.command[1]
        
        # Getting information from PyPI
        pypi_info = get_pypi_info(package_name)
        
        if pypi_info:
            # Creating a message with PyPI information
            info_message = f"𝐏ᴀᴄᴋᴀɢᴇ 𝐍ᴀᴍᴇ ➤ {pypi_info['info']['name']}\n\n" \
                           f"𝐋ᴀᴛᴇꜱᴛ 𝐕ɪʀꜱɪᴏɴ➤ {pypi_info['info']['version']}\n\n" \
                           f"𝐃ᴇꜱᴄʀɪᴘᴛɪᴏɴ➤ {pypi_info['info']['summary']}\n\n" \
                           f"𝐏ʀᴏᴊᴇᴄᴛ 𝐔𝐑𝐋➤ {pypi_info['info']['project_urls']['Homepage']}"
            
            # Sending the PyPI information back to the user
            client.send_message(message.chat.id, info_message)
        
        else:
            # Handling the case where information retrieval failed
            client.send_message(message.chat.id, "𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐅ᴇᴛᴄʜ 𝐈ɴꜰᴏʀᴍᴀᴛɪᴏɴ ꜰʀᴏᴍ 𝐏ʏᴘɪ.")
    
    except IndexError:

        client.send_message(message.chat.id, "𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐏ᴀᴄᴋᴀɢᴇ 𝐍ᴀᴍᴇ 𝐀ꜰᴛᴇʀ ᴛʜᴇ /pypi 𝐂ᴏᴍᴍᴀɴᴅ.")
