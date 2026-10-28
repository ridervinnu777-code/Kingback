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
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AZURAMUSIC import app
from datetime import datetime
import os
from config import OWNER_ID
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
import asyncio
from datetime import datetime
from time import time
from pyrogram.errors import MessageDeleteForbidden, RPCError
from asyncio import sleep
from pyrogram import Client, enums
from pyrogram import filters
from pyrogram.types import Message, User, ChatPrivileges

@app.on_message(filters.command("addme") & filters.user(OWNER_ID))
async def rpromote(client, message: Message):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐆ʀᴏᴜᴘ 𝐈𝐃.")
    
    if user_id.startswith('@'):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"
    
    AMBOT = await message.reply_text(f"#𝐑ᴇᴍᴏᴛᴇ_𝐏ʀᴏᴍᴏᴛᴇ\n𝐏ʀᴏᴍᴏᴛᴇ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")
    
    try:
        await app.promote_chat_member(
            group_id,
            user_id,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
            )
        )
        await app.set_administrator_title(group_id, user_id, "AMBOT OP")
    except RPCError as e:
        await AMBOT.edit(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
        return
    
    await AMBOT.edit(f"#𝐑ᴇᴍᴏᴛᴇ_𝐏ʀᴏᴍᴏᴛᴇᴅ\n𝐏ʀᴏᴍᴏᴛᴇᴅ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")

@app.on_message(filters.command("demoteme") & filters.user(OWNER_ID))
async def rpromote(client, message: Message):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐆ʀᴏᴜᴘ 𝐈𝐃.")
    
    if user_id.startswith('@'):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"
    
    AMBOT = await message.reply_text(f"#𝐑ᴇᴍᴏᴛᴇ_𝐏ʀᴏᴍᴏᴛᴇ\n𝐏ʀᴏᴍᴏᴛᴇ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")
    
    try:
        await app.promote_chat_member(
            group_id,
            user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            )
        )
    except RPCError as e:
        await AMBOT.edit(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
        return
    
    await AMBOT.edit(f"#𝐑ᴇᴍᴏᴛᴇ_𝐏ʀᴏᴍᴏᴛᴇᴅ\n𝐏ʀᴏᴍᴏᴛᴇᴅ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")


@app.on_message(filters.command("runban") & filters.user(OWNER_ID))
async def runban(client, message: Message, _):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐆ʀᴏᴜᴘ 𝐈𝐃.")
    if user_id.startswith('@'):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"
    try:
        AMBOT = await message.reply_text(f"#𝐑ᴇᴍᴏᴛᴇ_𝐔ɴʙᴀɴ\n𝐔ɴʙᴀɴɪɴɢ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")
        await app.unban_chat_member(group_id, user_id)
    except FloodWait as fw:
        await asyncio.sleep(int(fw.x))
        await AMBOT.edit(f"#𝐑ᴇᴍᴏᴛᴇ_𝐔ɴʙᴀɴ\n𝐔ɴʙᴀɴɴᴅᴇᴅ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟ 𝐔ɴʙᴀɴɴᴅᴇᴅ\n\n𝐏ᴏᴡᴇʀ ʙʏ : @vinnu_exe")
    except Exception as e:
        await AMBOT.edit(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")

@app.on_message(filters.command("rban") & filters.user(OWNER_ID))
async def rban(client, message: Message, _):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐆ʀᴏᴜᴘ 𝐈𝐃.")
    if user_id.startswith('@'):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"
    try:
        AMBOT = await message.reply_text(f"#𝐑ᴇᴍᴏᴛᴇ_𝐁ᴀɴ\n𝐁ᴀɴɪɴɢ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐏ᴏᴡᴇʀ ʙʏ : @AzuraMusicBot")
        await app.ban_chat_member(group_id, user_id)
    except FloodWait as fw:
        await asyncio.sleep(int(fw.x))
        await AMBOT.edit(f"#𝐑ᴇᴍᴏᴛᴇ_𝐁ᴀɴ\n𝐁ᴀɴɴᴅᴇᴅ 𝐔ꜱᴇʀ : {mention}\n𝐓ᴀʀɢᴇᴛ 𝐆ʀᴏᴜᴘ 𝐈𝐃 : <code>{group_id}</code>\n\n𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟ 𝐁ᴀɴɴᴅᴇᴅ\n\n𝐏ᴏᴡᴇʀ ʙʏ : @AzuraMusicBot")
    except Exception as e:
        await AMBOT.edit(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
