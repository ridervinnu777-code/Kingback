import asyncio
import logging
from pyrogram import filters
from pyrogram.enums import (
    ChatType,
    ChatMemberStatus,
    ParseMode,
    ChatMembersFilter,
)
from pyrogram.types import Message
from AZURAMUSIC import app

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

spam_chats = []


# ===================== ADMIN CHECK =====================

async def is_admin(chat_id, user_id):
    if not user_id:
        return False
    async for admin in app.get_chat_members(
        chat_id,
        filter=ChatMembersFilter.ADMINISTRATORS
    ):
        if admin.user and admin.user.id == user_id:
            return True
    return False


# ===================== MENTION USERS =====================

async def mention_users(client, message: Message, mode, text):
    chat_id = message.chat.id

    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text(
            "__𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐂ᴀɴ ʙᴇ 𝐔ꜱᴇᴅ ɪɴ 𝐆ʀᴏᴜᴘꜱ ᴀɴᴅ 𝐂ʜᴀɴɴᴇʟꜱ!__"
        )

    if text and message.reply_to_message:
        return await message.reply_text("__𝐆ɪᴠᴇ 𝐌ᴇ 𝐎ɴᴇ 𝐀ʀɢᴜᴍᴇɴᴛ!__")

    if text:
        mode = "text_on_cmd"
        msg_text = text
        reply_msg = None
    elif message.reply_to_message:
        mode = "text_on_reply"
        reply_msg = message.reply_to_message
        msg_text = None
    else:
        return await message.reply_text(
            "__𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴏʀ 𝐆ɪᴠᴇ 𝐌ᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ ᴛᴏ 𝐌ᴇɴᴛɪᴏɴ 𝐎ᴛʜᴇʀꜱ!__"
        )

    spam_chats.append(chat_id)

    usrnum = 0
    usrtxt = ""

    async for member in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break

        user = member.user
        if not user or user.is_bot:
            continue

        usrnum += 1
        name = user.first_name or "User"
        usrtxt += f"[{name}](tg://user?id={user.id}) "

        if usrnum == 5:
            if mode == "text_on_cmd":
                await client.send_message(
                    chat_id,
                    f"{usrtxt}\n\n{msg_text}",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True,
                )
            else:
                await reply_msg.reply_text(
                    usrtxt,
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True,
                )

            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except Exception:
        pass


# ===================== UTAG =====================

@app.on_message(filters.command("utag") & filters.group)
async def utag(_, message: Message):
    user_id = message.from_user.id if message.from_user else None
    if not await is_admin(message.chat.id, user_id):
        return await message.reply_text("❌ 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ.")

    text = None
    if len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    await mention_users(app, message, "text_on_cmd", text)


# ===================== ATAG =====================

@app.on_message(filters.command("atag") & filters.group)
async def atag(_, message: Message):
    user_id = message.from_user.id if message.from_user else None
    if not await is_admin(message.chat.id, user_id):
        return await message.reply_text("❌ 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ.")

    chat_id = message.chat.id

    try:
        members = []
        async for m in app.get_chat_members(chat_id):
            if m.status in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                user = m.user
                if user and not user.is_bot:
                    name = user.first_name or "Admin"
                    members.append(f"[{name}](tg://user?id={user.id})")
    except Exception:
        return await message.reply_text("__𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐅ᴇᴛᴄʜ 𝐏ᴀʀᴛɪᴄɪᴘᴀɴᴛꜱ!__")

    if not members:
        return await message.reply_text(
            "__𝐍ᴏ 𝐀ᴅᴍɪɴꜱ 𝐅ᴏᴜɴᴅ ɪɴ 𝐓ʜɪꜱ 𝐆ʀᴏᴜᴘ ᴏʀ 𝐂ʜᴀɴɴᴇʟ!__"
        )

    admin_text = ", ".join(members)

    if len(message.command) > 1:
        text = message.text.split(None, 1)[1]
        await message.reply_text(
            f"{admin_text}\n\n{text}",
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
    elif message.reply_to_message:
        await message.reply_to_message.reply_text(
            admin_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )
    else:
        await message.reply_text(
            admin_text,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True,
        )


# ===================== CANCEL =====================

@app.on_message(filters.command("ucancel") & filters.group)
async def cancel_spam(_, message: Message):
    user_id = message.from_user.id if message.from_user else None
    if not await is_admin(message.chat.id, user_id):
        return await message.reply_text("❌ 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ.")

    chat_id = message.chat.id

    if chat_id not in spam_chats:
        return await message.reply_text(
            "__𝐓ʜᴇʀᴇ ɪꜱ 𝐍ᴏ 𝐏ʀᴏᴄᴇꜱꜱ 𝐎ɴɢᴏɪɴɢ...__"
        )

    try:
        spam_chats.remove(chat_id)
    except Exception:
        pass

    await message.reply_text("__𝐒ᴛᴏᴘᴘᴇᴅ.__")
