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
import random
from pyrogram.types import Message
from AZURAMUSIC import app
from AZURAMUSIC.plugins.tools.pretenderdb import (
    impo_off, impo_on, check_pretender,
    add_userdata, get_userdata, usr_data
)
from AZURAMUSIC.utils.admin_filters import admin_filter
from config import SHASHANK_IMG



@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**🔓 𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐃ᴇᴛᴇᴄᴛᴇᴅ 🔓**
━━━━━━━━━━━━━━━  
**🍊 𝐍ᴀᴍᴇ** : {message.from_user.mention}
**🍅 𝐔ꜱᴇʀ 𝐈𝐃** : {message.from_user.id}
━━━━━━━━━━━━━━━  \n
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "NO USERNAME"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "NO USERNAME"
        )
        msg += """
**🐻‍❄️ 𝐂ʜᴀɴɢᴇᴅ 𝐔ꜱᴇʀɴᴀᴍᴇ 🐻‍❄️**
━━━━━━━━━━━━━━━  
**🎭 𝐅ʀᴏᴍ** : {bef}
**🍜 𝐓ᴏ** : {aft}
━━━━━━━━━━━━━━━  \n
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**🪧 𝐂ʜᴀɴɢᴇꜱ 𝐅ɪʀꜱᴛ 𝐍ᴀᴍᴇ 🪧**
━━━━━━━━━━━━━━━  
**🔐 𝐅ʀᴏᴍ** : {bef}
**🍓 𝐓ᴏ** : {aft}
━━━━━━━━━━━━━━━  \n
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "NO LAST NAME"
        lastname_after = message.from_user.last_name or "NO LAST NAME"
        msg += """
**🪧 𝐂ʜᴀɴɢᴇꜱ 𝐋ᴀꜱᴛ 𝐍ᴀᴍᴇ 🪧**
━━━━━━━━━━━━━━━  
**🚏𝐅ʀᴏᴍ** : {bef}
**🍕 𝐓ᴏ** : {aft}
━━━━━━━━━━━━━━━  \n
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random. choice(SHASHANK_IMG), caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot & admin_filter)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("𝐃ᴇᴛᴇᴄᴛ 𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐔ꜱᴇʀꜱ **𝐔ꜱᴀɢᴇ:** `/imposter enable|disable`")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐌ᴏᴅᴇ ɪꜱ 𝐀ʟʀᴇᴀᴅʏ 𝐄ɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐄ɴᴀʙʟᴇᴅ 𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐌ᴏᴅᴇ ꜰᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐌ᴏᴅᴇ ɪꜱ 𝐀ʟʀᴇᴀᴅʏ 𝐃ɪꜱᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐃ɪꜱᴀʙʟᴇᴅ 𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐌ᴏᴅᴇ ꜰᴏʀ** {message.chat.title}")
    else:
        await message.reply("**𝐃ᴇᴛᴇᴄᴛ 𝐏ʀᴇᴛᴇɴᴅᴇʀ 𝐔ꜱᴇʀꜱ 𝐔ꜱᴀɢᴇ : 𝐏ʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|𝐎ꜰꜰ**")
