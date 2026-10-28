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
from AZURAMUSIC.misc import SUDOERS
from AZURAMUSIC.utils.database import get_lang, is_maintenance
from strings import get_string


def language(mystic):
    async def wrapper(_, message, **kwargs):
        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} 𝐈ꜱ 𝐔ɴᴅᴇʀ 𝐌ᴀɪɴᴛᴇɴᴀɴᴄᴇ, 𝐕ɪꜱɪᴛ <ᴀ 𝐇ʀᴇꜰ={SUPPORT_CHAT}>𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ</a> ꜰᴏʀ 𝐊ɴᴏᴡɪɴɢ ᴛʜᴇ 𝐑ᴇᴀꜱᴏɴ.",
                    disable_web_page_preview=True,
                )
        try:
            await message.delete()
        except:
            pass

        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        if await is_maintenance() is False:
            if CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} 𝐈ꜱ 𝐔ɴᴅᴇʀ 𝐌ᴀɪɴᴛᴇɴᴀɴᴄᴇ, 𝐕ɪꜱɪᴛ 𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ ꜰᴏʀ 𝐊ɴᴏᴡɪɴɢ ᴛʜᴇ 𝐑ᴇᴀꜱᴏɴ.",
                    show_alert=True,
                )
        try:
            language = await get_lang(CallbackQuery.message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, CallbackQuery, language)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            language = await get_lang(message.chat.id)
            language = get_string(language)
        except:
            language = get_string("en")
        return await mystic(_, message, language)

    return wrapper
