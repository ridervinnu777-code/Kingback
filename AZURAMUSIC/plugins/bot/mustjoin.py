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
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AZURAMUSIC import app

#--------------------------

# Force-join is OFF. To turn it ON again, put a channel/group username here,
# for example:  MUST_JOIN = "zaxpk"
MUST_JOIN = ""
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/d24262661dda3f1832290.jpg", caption=f"๏ 𝐀ᴄᴄᴏʀᴅɪɴɢ ᴛᴏ 𝐌ʏ 𝐃ᴀᴛᴀʙᴀꜱᴇ 𝐘ᴏᴜ'ᴠᴇ 𝐍ᴏᴛ 𝐉ᴏɪɴᴇᴅ [๏𝐒ᴜᴘᴘᴏʀᴛ๏]({link}) 𝐘ᴇᴛ, ɪꜰ 𝐘ᴏᴜ 𝐖ᴀɴᴛ ᴛᴏ 𝐔ꜱᴇ 𝐌ᴇ 𝐓ʜᴇɴ 𝐉ᴏɪɴ [๏𝐒ᴜᴘᴘᴏʀᴛ๏]({link}) 𝐀ɴᴅ 𝐒ᴛᴀʀᴛ 𝐌ᴇ 𝐀ɢᴀɪɴ ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏𝐉ᴏɪɴ๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
