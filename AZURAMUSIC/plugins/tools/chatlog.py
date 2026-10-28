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

import random
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from pyrogram.errors import RPCError
from config import LOGGER_ID as LOG_GROUP_ID
from AZURAMUSIC import app

photo = [
    "https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
    "https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
    "https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
    "https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
    "https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
]


@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    chat = message.chat

    for member in message.new_chat_members:
        if member.id != app.id:
            continue

        try:
            count = await app.get_chat_members_count(chat.id)
        except RPCError:
            count = "Unavailable"

        try:
            link = await app.export_chat_invite_link(chat.id)
        except RPCError:
            link = None

        chat_username = (
            f"@{chat.username}"
            if chat.username
            else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
        )

        chat_link = (
            f'<𝐀 𝐇ʀᴇꜰ="{link}">𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ</a>'
            if link
            else "𝐔ɴᴀᴠᴀɪʟᴀʙʟᴇ"
        )

        added_by = (
            message.from_user.mention
            if message.from_user
            else "𝐔ɴᴋɴᴏᴡɴ 𝐔ꜱᴇʀ"
        )

        msg = (
            "╭━━━〔 🌸 ˹ 𝐀ᴢᴜʀᴀ ✘ 𝐌ᴜsɪᴄ ˼〕━━━╮\n"
            "┃\n"
            "┃ 🎵 <b>𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ ɪɴ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ</b>\n"
            "┃\n"
            f"┃ 📌 <b>𝐂ʜᴀᴛ:</b> {chat.title}\n"
            f"┃ 🆔 <b>𝐈𝐃:</b> <code>{chat.id}</code>\n"
            f"┃ 🔐 <b>𝐔ꜱᴇʀɴᴀᴍᴇ:</b> {chat_username}\n"
            f"┃ 🛰 <b>𝐋ɪɴᴋ:</b> {chat_link}\n"
            f"┃ 👥 <b>𝐌ᴇᴍʙᴇʀꜱ:</b> {count}\n"
            f"┃ 👤 <b>𝐀ᴅᴅᴇᴅ ʙʏ:</b> {added_by}\n"
            "┃\n"
            "╰━━━━━━━━━━━━━━━━━━━━━━╯"
        )

        buttons = []
        if link:
            buttons = [[
                InlineKeyboardButton(
                    "👀 𝐕ɪᴇᴡ 𝐆ʀᴏᴜᴘ",
                    url=link,
                    style=ButtonStyle.DANGER
                )
            ]]

        await app.send_photo(
            LOG_GROUP_ID,
            photo=random.choice(photo),
            caption=msg,
            reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
        )


@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    try:
        me = await app.get_me()

        if message.left_chat_member.id != me.id:
            return

        remove_by = (
            message.from_user.mention
            if message.from_user
            else "𝐔ɴᴋɴᴏᴡɴ 𝐔ꜱᴇʀ"
        )

        title = message.chat.title or "𝐔ɴᴋɴᴏᴡɴ 𝐂ʜᴀᴛ"

        username = (
            f"@{message.chat.username}"
            if message.chat.username
            else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        )

        chat_id = message.chat.id

        left = (
            "╭━━━〔 🚫 ˹ 𝐀ᴢᴜʀᴀ ✘ 𝐌ᴜsɪᴄ ˼〕━━━╮\n"
            "┃\n"
            "┃ <b>#𝐋ᴇꜰᴛ_𝐆ʀᴏᴜᴘ</b>\n"
            "┃\n"
            f"┃ 📌 <b>𝐂ʜᴀᴛ:</b> {title}\n"
            f"┃ 🆔 <b>𝐈𝐃:</b> <code>{chat_id}</code>\n"
            f"┃ 🔐 <b>𝐔ꜱᴇʀɴᴀᴍᴇ:</b> {username}\n"
            f"┃ 👤 <b>𝐑ᴇᴍᴏᴠᴇᴅ ʙʏ:</b> {remove_by}\n"
            f"┃ 🤖 <b>𝐁ᴏᴛ:</b> @{app.username}\n"
            "┃\n"
            "╰━━━━━━━━━━━━━━━━━━━━━━╯"
        )

        await app.send_photo(
            LOG_GROUP_ID,
            photo=random.choice(photo),
            caption=left,
        )

    except RPCError:
        return
    except Exception:
        return
