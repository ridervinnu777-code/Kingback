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
from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)
import datetime
from AZURAMUSIC import app

# ── KripanshEmojis_by_fStikBot pack IDs ──
_KE_OK    = 6129812419028982717   # ✅
_KE_WARN  = 6129782440157256336   # ⚠️
_KE_CROWN = 6129705083501293112   # 👑
_KE_BLOCK = 6129840374971112593   # 🚫
_KE_FIRE  = 6129792056589031358   # 🔥

def ke(eid, fb):
    return f'<emoji id={eid}>{fb}</emoji>'


@app.on_callback_query(filters.regex(r"^unpin"))
async def unpin_callbacc(client, CallbackQuery):
    user_id = CallbackQuery.from_user.id
    name = CallbackQuery.from_user.first_name
    chat_id = CallbackQuery.message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            await CallbackQuery.answer("⚠️ 𝐘ᴏᴜ 𝐃ᴏɴᴛ 𝐇ᴀᴠᴇ 𝐑ɪɢʜᴛꜱ, 𝐁ᴀᴋᴀ!", show_alert=True)
            return
    else:
        await CallbackQuery.answer("⚠️ 𝐘ᴏᴜ 𝐃ᴏɴᴛ 𝐇ᴀᴠᴇ 𝐑ɪɢʜᴛꜱ, 𝐁ᴀᴋᴀ!", show_alert=True)
        return
    
    msg_id = CallbackQuery.data.split("=")[1]
    try:
        msg_id = int(msg_id)
    except:
        if msg_id == "yes":
            await client.unpin_all_chat_messages(chat_id)
            textt = "I have unpinned all the pinned messages"
        else:
            textt = "Ok, i wont unpin all the messages"

        await CallbackQuery.message.edit_caption(
            textt,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="𝐃ᴇʟᴇᴛᴇ", callback_data="delete_btn=admin")]
                ]
            )
        )
        return
        
    await client.unpin_chat_message(chat_id, msg_id)
    await CallbackQuery.message.edit_caption(
        "𝐔ɴᴘɪɴɴᴇᴅ!!", 
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="𝐃ᴇʟᴇᴛᴇ", callback_data="delete_btn=admin")]
            ]
        )
    )

@app.on_message(filters.command(["unpinall"]))
async def unpin_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            return await message.reply_text(f"{ke(_KE_BLOCK,'🚫')} <b>𝐘ᴏᴜ 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ 𝐔ɴᴘɪɴ 𝐒ᴏᴍᴇᴛʜɪɴɢ</b>")
    else:
        return await message.reply_text(f"{ke(_KE_BLOCK,'🚫')} <b>𝐘ᴏᴜ 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ 𝐔ɴᴘɪɴ 𝐒ᴏᴍᴇᴛʜɪɴɢ</b>")

    await message.reply_text(
        f"{ke(_KE_WARN,'⚠️')} {ke(_KE_FIRE,'🔥')} <b>𝐀ʀᴇ 𝐘ᴏᴜ 𝐒ᴜʀᴇ 𝐘ᴏᴜ 𝐖ᴀɴᴛ ᴛᴏ 𝐔ɴᴘɪɴ 𝐀ʟʟ ᴛʜᴇ 𝐏ɪɴɴᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇꜱ ɪɴ 𝐓ʜɪꜱ 𝐂ʜᴀᴛ?</b>",
        reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton(text="𝗬𝗘𝗦", callback_data="unpinall=yes"),
                    InlineKeyboardButton(text="𝗡𝗢", callback_data="unpinall=no")
                ]
            ]
        )
    )
