# -----------------------------------------------
# 🔸 Queue Empty & Auto Direct Play Handler
# -----------------------------------------------
import random
from pyrogram import filters, enums
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from AZURAMUSIC import app

RANDOM_SONGS = [
    "Tu Mera Hai Sanam",
    "Kesariya",
    "Raataan Lambiyan",
    "Tum Hi Ho",
    "Apna Bana Le",
    "Heeriye",
    "O Bedardeya",
    "Chaleya",
    "Satranga",
    "Tere Vaaste"
]

async def send_queue_empty_msg(chat_id: int):
    """Sends stylized blockquote message when queue ends."""
    
    bot_mention = f"<𝐀 𝐇ʀᴇꜰ='𝐓𝐆://𝐔ꜱᴇʀ?𝐈𝐃={app.id}'>𝐀ᴢᴜʀᴀ</a>"
    
    empty_text = (
        f"<blockquote>"
        f"🎵 ╭──〔 💖 𝐐ᴜᴇᴜᴇ 𝐄ᴍᴘᴛʏ 〕\n"
        f"│\n"
        f"├ 💕 ⇛ 𝐐ᴜᴇᴜᴇ 𝐊ʜᴀᴛᴀᴍ 𝐁ᴇʙᴇꜱ!\n"
        f"├ 🎶 ⇛ 𝐒ᴏɴɢꜱ 𝐊ʜᴀᴛᴀᴍ 𝐇ᴏ 𝐆ᴀʏᴇ 𝐇ᴀɪɴ, 𝐂ᴜᴛɪᴇ.\n"
        f"├ 💿 ⇛ 𝐀ᴜʀ 𝐒ᴜɴɴᴀ 𝐇ᴀɪ ᴛᴏ 𝐍ɪᴄʜᴇ 𝐂ʟɪᴄᴋ 𝐊ᴀʀᴏ.\n"
        f"│\n"
        f"🌸 ╰── 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ {bot_mention}"
        f"</blockquote>"
    )

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="˹𝐏ʟᴀʏ 𝐌ᴏʀᴇ˼",
                callback_data="auto_play_random_song",
                style=ButtonStyle.PRIMARY,
            )
        ]
    ])

    try:
        await app.send_message(
            chat_id=chat_id,
            text=empty_text,
            parse_mode=enums.ParseMode.HTML,
            reply_markup=buttons
        )
    except Exception:
        pass


@app.on_callback_query(filters.regex("^auto_play_random_song$"))
async def play_more_button_click(client, query: CallbackQuery):
    selected_song = random.choice(RANDOM_SONGS)
    await query.answer(f"🎵 𝐑ᴀɴᴅᴏᴍ 𝐒ᴏɴɢ 𝐏ɪᴄᴋᴇᴅ: {selected_song}\n𝐒ᴇɴᴅ /play {selected_song}", show_alert=True)
    
