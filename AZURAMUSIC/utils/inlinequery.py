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

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="𝐏ᴀᴜꜱᴇ",
            description=f"𝐏ᴀᴜꜱᴇ ᴛʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ ᴏɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="𝐑ᴇꜱᴜᴍᴇ",
            description=f"𝐑ᴇꜱᴜᴍᴇ ᴛʜᴇ 𝐏ᴀᴜꜱᴇᴅ 𝐒ᴛʀᴇᴀᴍ ᴏɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="𝐒ᴋɪᴘ",
            description=f"𝐒ᴋɪᴘ ᴛʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ ᴏɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ ᴀɴᴅ 𝐌ᴏᴠᴇꜱ ᴛᴏ ᴛʜᴇ 𝐍ᴇxᴛ 𝐒ᴛʀᴇᴀᴍ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ",
            description="𝐄ɴᴅ ᴛʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐒ᴛʀᴇᴀᴍ ᴏɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="𝐒ʜᴜꜰꜰʟᴇ",
            description="𝐒ʜᴜꜰꜰʟᴇ ᴛʜᴇ 𝐐ᴜᴇᴜᴇᴅ 𝐒ᴏɴɢꜱ ɪɴ 𝐏ʟᴀʏʟɪꜱᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="𝐋ᴏᴏᴘ",
            description="𝐋ᴏᴏᴘ ᴛʜᴇ 𝐂ᴜʀʀᴇɴᴛ 𝐏ʟᴀʏɪɴɢ 𝐓ʀᴀᴄᴋ ᴏɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
