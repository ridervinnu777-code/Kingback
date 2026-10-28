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
import aiohttp
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from AZURAMUSIC import app


@app.on_message(filters.command(["github", "git"]))
async def github(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text("**𝐔ꜱᴀɢᴇ:** `/git <username>`")

    username = message.text.split(None, 1)[1]
    url = f"https://api.github.com/users/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 404:
                return await message.reply_text("🚫 **𝐔ꜱᴇʀ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ!**")
            elif response.status != 200:
                return await message.reply_text("⚠️ **𝐄ʀʀᴏʀ 𝐅ᴇᴛᴄʜɪɴɢ 𝐃ᴀᴛᴀ!**")

            data = await response.json()

    name = data.get("name", "Not specified")
    bio = data.get("bio", "No bio available.")
    blog = data.get("blog", "N/A")
    location = data.get("location", "Unknown")
    company = data.get("company", "N/A")
    created = data.get("created_at", "N/A")
    url = data.get("html_url", "N/A")
    repos = data.get("public_repos", "0")
    followers = data.get("followers", "0")
    following = data.get("following", "0")
    avatar = data.get("avatar_url", None)

    caption = f"""
✨ **𝐆ɪᴛʜᴜʙ 𝐏ʀᴏꜰɪʟᴇ 𝐈ɴꜰᴏ**

👤 **𝐍ᴀᴍᴇ:** `{name}`
🔧 **ᴜsᴇʀɴᴀᴍᴇ:** `{username}`
📌 **𝐁ɪᴏ:** {bio}
🏢 **𝐂ᴏᴍᴘᴀɴʏ:** {company}
📍 **𝐋ᴏᴄᴀᴛɪᴏɴ:** {location}
🌐 **𝐁ʟᴏɢ:** {blog}
🗓 **𝐂ʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created}`
📁 **ᴘᴜʙʟɪᴄ ʀᴇᴘᴏs:** `{repos}`
👥 **ғᴏʟʟᴏᴡᴇʀs:** `{followers}` | **ғᴏʟʟᴏᴡɪɴɢ:** `{following}`
🔗 **𝐏ʀᴏꜰɪʟᴇ:** [𝐕ɪᴇᴡ ᴏɴ 𝐆ɪᴛʜᴜʙ]({url})
""".strip()

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("❌ 𝐂ʟᴏꜱᴇ", callback_data="close")]]
    )

    if avatar:
        await message.reply_photo(photo=avatar, caption=caption, reply_markup=keyboard)
    else:
        await message.reply_text(caption, reply_markup=keyboard)
