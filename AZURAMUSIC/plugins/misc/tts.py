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

import io
from gtts import gTTS
from pyrogram import filters
from AZURAMUSIC import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ ᴛᴏ 𝐂ᴏɴᴠᴇʀᴛ ᴛᴏ 𝐒ᴘᴇᴇᴄʜ."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="hi")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "audio.mp3"
    await message.reply_audio(audio_file)

