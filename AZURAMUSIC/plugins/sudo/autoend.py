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
from pyrogram import filters
from pyrogram.types import Message
from AZURAMUSIC import app
from AZURAMUSIC.misc import SUDOERS
from AZURAMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>𝐄xᴀᴍᴘʟᴇ :</b>\n\n/autoend [𝐄ɴᴀʙʟᴇ | 𝐃ɪꜱᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» 𝐀ᴜᴛᴏ 𝐄ɴᴅ 𝐒ᴛʀᴇᴀᴍ 𝐄ɴᴀʙʟᴇᴅ.\n\n𝐀ꜱꜱɪꜱᴛᴀɴᴛ 𝐖ɪʟʟ 𝐀ᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ 𝐋ᴇᴀᴠᴇ ᴛʜᴇ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ 𝐀ꜰᴛᴇʀ 𝐅ᴇᴡ 𝐌ɪɴꜱ 𝐖ʜᴇɴ 𝐍ᴏ 𝐎ɴᴇ ɪꜱ 𝐋ɪꜱᴛᴇɴɪɴɢ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» 𝐀ᴜᴛᴏ 𝐄ɴᴅ 𝐒ᴛʀᴇᴀᴍ 𝐃ɪꜱᴀʙʟᴇᴅ.")
    else:
        await message.reply_text(usage)
