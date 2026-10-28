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
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from config import OWNER_ID as owner_id
from AZURAMUSIC import app


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@app.on_message(filters.command("bug"))
async def bugs(_, msg: Message):
    if msg.chat.username:
        chat_username = f"@{msg.chat.username}/`{msg.chat.id}`"
    else:
        chat_username = f"𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ/`{msg.chat.id}`"

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        "[" + msg.from_user.first_name + "](tg://user?id=" + str(msg.from_user.id) + ")"
    )
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    

    bug_report = f"""
**#𝐁ᴜɢ : ** **𝐓𝐆://𝐔ꜱᴇʀ?𝐈𝐃={owner_id}**

**𝐑ᴇᴘᴏʀᴛᴇᴅ ʙʏ : ** **{mention}**
**𝐔ꜱᴇʀ 𝐈𝐃 : ** **{user_id}**
**𝐂ʜᴀᴛ : ** **{chat_username}**

**𝐁ᴜɢ : ** **{bugs}**

**𝐄ᴠᴇɴᴛ 𝐒ᴛᴀᴍᴘ : ** **{datetimes}**"""

    if msg.chat.type == "private":
        await msg.reply_text("<b>» 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ ɪꜱ 𝐎ɴʟʏ ꜰᴏʀ 𝐆ʀᴏᴜᴘꜱ.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>» 𝐀ʀᴇ 𝐘ᴏᴜ 𝐂ᴏᴍᴇᴅʏ 𝐌ᴇ 🤣, 𝐘ᴏᴜ'ʀᴇ ᴛʜᴇ 𝐎ᴡɴᴇʀ ᴏꜰ ᴛʜᴇ 𝐁ᴏᴛ.</b>",
            )
            return
        else:
            await msg.reply_text("𝐂ʜᴜᴍᴛɪʏᴀ 𝐎ᴡɴᴇʀ!")
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>𝐁ᴜɢ 𝐑ᴇᴘᴏʀᴛ : {bugs}</b>\n\n"
                "<b>» 𝐁ᴜɢ 𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐑ᴇᴘᴏʀᴛᴇᴅ ᴀᴛ 𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✦ 𝐂ʟᴏꜱᴇ ✦", callback_data="close_data")]]
                ),
            )
            await app.send_photo(
                -1004413083427,
                photo="https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/4e49edcd-01b8-4c42-98e9-41c1d142b432.jpg",
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("✦ 𝐕ɪᴇᴡ 𝐁ᴜɢ ✦", url=f"{msg.link}")],
                        [
                            InlineKeyboardButton(
                                "✦ 𝐂ʟᴏꜱᴇ ✦", callback_data="close_send_photo"
                            )
                        ],
                    ]
                ),
            )
        else:
            await msg.reply_text(
                f"<b>» 𝐍ᴏ 𝐁ᴜɢ ᴛᴏ 𝐑ᴇᴘᴏʀᴛ !</b>",
            )




@app.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_,  query :CallbackQuery):
    is_admin = await app.get_chat_member(query.message.chat.id, query.from_user.id)
    if not is_admin.privileges.can_delete_messages:
        await query.answer("𝐘ᴏᴜ 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʟᴏꜱᴇ 𝐓ʜɪꜱ.", show_alert=True)
    else:
        await query.message.delete()


