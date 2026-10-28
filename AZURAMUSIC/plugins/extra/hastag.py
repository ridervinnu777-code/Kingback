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
import requests
from bs4 import BeautifulSoup as  BSP
from AZURAMUSIC import app as AZURA
from pyrogram import filters
url = "https://all-hashtag.com/library/contents/ajax_generator.php"

@AZURA.on_message(filters.command("hastag"))
async def hastag(bot, message):
    global content
    try:
        text = message.text.split(' ',1)[1]
        data = dict(keyword=text, filter="top")

        res = requests.post(url, data).text

        content = BSP(res, 'html.parser').find("div", {"class":"copy-hashtags"}).string
    except IndexError:
        return await message.reply_text("𝐄xᴀᴍᴘʟᴇ:\n\n/hastag 𝐏ʏᴛʜᴏɴ")
        
    
    await message.reply_text(f"𝐇ᴇʀᴇ ɪꜱ 𝐘ᴏᴜʀ  𝐇ᴀꜱᴛᴀɢ :\n<pre>{content}</pre>", quote=True)
    
mod_name = "𝐇ᴀꜱʜᴛᴀɢ"
help= """
𝐘ᴏᴜ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ 𝐇ᴀꜱʜᴛᴀɢ 𝐆ᴇɴᴇʀᴀᴛᴏʀ 𝐖ʜɪᴄʜ 𝐖ɪʟʟ 𝐆ɪᴠᴇ 𝐘ᴏᴜ ᴛʜᴇ 𝐓ᴏᴘ 𝟹𝟶 ᴀɴᴅ 𝐌ᴏʀᴇ 𝐇ᴀꜱʜᴛᴀɢꜱ 𝐁ᴀꜱᴇᴅ 𝐎ꜰꜰ ᴏꜰ 𝐎ɴᴇ 𝐊ᴇʏᴡᴏʀᴅ 𝐒ᴇʟᴇᴄᴛɪᴏɴ.
° /hastag 𝐄ɴᴛᴇʀ 𝐖ᴏʀᴅ ᴛᴏ 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐇ᴀꜱᴛᴀɢ.
°𝐄xᴀᴍᴘʟᴇ:  /hastag 𝐏ʏᴛʜᴏɴ """
