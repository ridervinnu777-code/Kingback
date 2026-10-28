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
from pyrogram import filters, Client, enums
from AZURAMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from AZURAMUSIC.mongo.nightmodedb import nightdb, nightmode_on, nightmode_off, get_nightchats 


CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_change_info=False,
    can_add_web_page_previews=False,
    can_pin_messages=False,
    can_invite_users=False
)

OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=True,
    can_add_web_page_previews=True,
    can_pin_messages=True,
    can_invite_users=True
)

buttons = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("๏ 𝐄ɴᴀʙʟᴇ ๏", callback_data="add_night"),
        InlineKeyboardButton("๏ 𝐃ɪꜱᴀʙʟᴇ ๏", callback_data="rm_night")
    ]]
)

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(
        photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
        caption="**𝐂ʟɪᴄᴋ ᴏɴ ᴛʜᴇ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ ᴛᴏ 𝐄ɴᴀʙʟᴇ ᴏʀ 𝐃ɪꜱᴀʙʟᴇ 𝐍ɪɢʜᴛᴍᴏᴅᴇ ɪɴ 𝐓ʜɪꜱ 𝐂ʜᴀᴛ.**",
        reply_markup=buttons
    )


@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query: CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id

    check_night = await nightdb.find_one({"chat_id": chat_id})

    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)

    if user_id not in administrators:
        return await query.answer("❌ 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ!", show_alert=True)

    if data == "add_night":
        if check_night:
            await query.message.edit_caption("**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐀ʟʀᴇᴀᴅʏ 𝐄ɴᴀʙʟᴇᴅ.**")
        else:
            await nightmode_on(chat_id)
            await query.message.edit_caption(
                "**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐄ɴᴀʙʟᴇᴅ!\n\n"
                "𝐆ʀᴏᴜᴘ 𝐖ɪʟʟ 𝐂ʟᴏꜱᴇ ᴀᴛ 12𝐀ᴍ ᴀɴᴅ 𝐎ᴘᴇɴ ᴀᴛ 06𝐀ᴍ [𝐈𝐒𝐓].**"
            )

    elif data == "rm_night":
        if check_night:
            await nightmode_off(chat_id)
            await query.message.edit_caption("**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐃ɪꜱᴀʙʟᴇᴅ!**")
        else:
            await query.message.edit_caption("**๏ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐀ʟʀᴇᴀᴅʏ 𝐎ꜰꜰ.**")


async def start_nightmode():
    schats = await get_nightchats()
    for chat in schats:
        chat_id = int(chat["chat_id"])
        try:
            await app.send_photo(
                chat_id,
                photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                caption="**𝐌ᴀʏ ᴛʜᴇ 𝐀ɴɢᴇʟꜱ ꜰʀᴏᴍ 𝐇ᴇᴀᴠᴇɴ 𝐁ʀɪɴɢ ᴛʜᴇ 𝐒ᴡᴇᴇᴛᴇꜱᴛ ᴏꜰ 𝐀ʟʟ 𝐃ʀᴇᴀᴍꜱ ꜰᴏʀ 𝐘ᴏᴜ. 𝐌ᴀʏ 𝐘ᴏᴜ 𝐇ᴀᴠᴇ 𝐋ᴏɴɢ ᴀɴᴅ 𝐁ʟɪꜱꜱꜰᴜʟ 𝐒ʟᴇᴇᴘ 𝐅ᴜʟʟ ᴏꜰ 𝐇ᴀᴘᴘʏ 𝐃ʀᴇᴀᴍꜱ.\n\n𝐆ʀᴏᴜᴘ ɪꜱ 𝐂ʟᴏꜱɪɴɢ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐄ᴠᴇʀʏᴏɴᴇ  !**"
            )
            await app.set_chat_permissions(chat_id, CLOSE_CHAT)
        except Exception as e:
            print(f"Unable to close group {chat_id}: {e}")


async def close_nightmode():
    schats = await get_nightchats()
    for chat in schats:
        chat_id = int(chat["chat_id"])
        try:
            await app.send_photo(
                chat_id,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption="**𝐆ʀᴏᴜᴘ ɪꜱ 𝐎ᴘᴇɴɪɴɢ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐄ᴠᴇʀʏᴏɴᴇ !\n\n𝐌ᴀʏ 𝐓ʜɪꜱ 𝐃ᴀʏ 𝐂ᴏᴍᴇ ᴡɪᴛʜ 𝐀ʟʟ ᴛʜᴇ 𝐋ᴏᴠᴇ 𝐘ᴏᴜʀ 𝐇ᴇᴀʀᴛ 𝐂ᴀɴ 𝐇ᴏʟᴅ ᴀɴᴅ 𝐁ʀɪɴɢ 𝐘ᴏᴜ 𝐄ᴠᴇʀʏ 𝐒ᴜᴄᴄᴇꜱꜱ 𝐘ᴏᴜ 𝐃ᴇꜱɪʀᴇ. 𝐌ᴀʏ 𝐄ᴀᴄʜ ᴏꜰ 𝐘ᴏᴜʀ 𝐅ᴏᴏᴛꜱᴛᴇᴘꜱ 𝐁ʀɪɴɢ 𝐉ᴏʏ ᴛᴏ ᴛʜᴇ 𝐄ᴀʀᴛʜ ᴀɴᴅ 𝐘ᴏᴜʀꜱᴇʟꜰ. 𝐈 𝐖ɪꜱʜ 𝐘ᴏᴜ ᴀ 𝐌ᴀɢɪᴄᴀʟ 𝐃ᴀʏ ᴀɴᴅ ᴀ 𝐖ᴏɴᴅᴇʀꜰᴜʟ 𝐋ɪꜰᴇ 𝐀ʜᴇᴀᴅ.**"
            )
            await app.set_chat_permissions(chat_id, OPEN_CHAT)
        except Exception as e:
            print(f"Unable to open group {chat_id}: {e}")


scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()
