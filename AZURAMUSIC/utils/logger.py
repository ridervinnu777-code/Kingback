from pyrogram.enums import ParseMode
from AZURAMUSIC import app
from AZURAMUSIC.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if not await is_on_off(2):
        return

    # Safe values
    chat = message.chat
    user = message.from_user

    chat_id = chat.id
    chat_name = chat.title or "Private Chat"
    chat_username = f"@{chat.username}" if chat.username else "None"

    if user:
        user_id = user.id
        user_name = user.mention or "Unknown"
        username = f"@{user.username}" if user.username else "None"
    else:
        user_id = "Unknown"
        user_name = "Unknown"
        username = "None"

    # Safe query extraction
    query = ""
    if message.text:
        parts = message.text.split(None, 1)
        if len(parts) > 1:
            query = parts[1].strip()

    if not query:
        query = "No query provided"

    logger_text = f"""
<b>{app.mention} 𝐏ʟᴀʏ 𝐋ᴏɢ</b>

<b>𝐂ʜᴀᴛ 𝐈𝐃 :</b> <code>{chat_id}</code>
<b>𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ :</b> {chat_name}
<b>𝐂ʜᴀᴛ 𝐔ꜱᴇʀɴᴀᴍᴇ :</b> {chat_username}

<b>𝐔ꜱᴇʀ 𝐈𝐃 :</b> <code>{user_id}</code>
<b>𝐍ᴀᴍᴇ :</b> {user_name}
<b>𝐔ꜱᴇʀɴᴀᴍᴇ :</b> {username}

<b>𝐐ᴜᴇʀʏ :</b> {query}
<b>𝐒ᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}
"""

    if chat_id != LOGGER_ID:
        try:
            await app.send_message(
                chat_id=LOGGER_ID,
                text=logger_text,
                parse_mode=ParseMode.HTML,
                disable_web_page_preview=True,
            )
        except Exception:
            pass
