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
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from unidecode import unidecode
from AZURAMUSIC import app
from AZURAMUSIC.misc import SUDOERS
from AZURAMUSIC.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["activevc", "activevoice","vc"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» 𝐆ᴇᴛᴛɪɴɢ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛꜱ 𝐋ɪꜱᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a>\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()}\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝐍ᴏ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛꜱ ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝐋ɪꜱᴛ ᴏꜰ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐀ᴄᴛɪᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜᴀᴛꜱ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo","vvc"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» 𝐆ᴇᴛᴛɪɴɢ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛꜱ 𝐋ɪꜱᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» 𝐍ᴏ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛꜱ ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» 𝐋ɪꜱᴛ ᴏꜰ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐀ᴄᴛɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜᴀᴛꜱ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )

@app.on_message(filters.command(["ac","av"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(f"✫ <b><u>𝐀ᴄᴛɪᴠᴇ 𝐂ʜᴀᴛꜱ 𝐈ɴꜰᴏ</u></b> :\n\n𝐕ᴏɪᴄᴇ : {ac_audio}\n𝐕ɪᴅᴇᴏ  : {ac_video}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('✦ 𝐂ʟᴏꜱᴇ ✦', callback_data=f"close")]]))
