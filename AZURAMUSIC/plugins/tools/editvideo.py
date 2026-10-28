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
import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pydub import AudioSegment
from AZURAMUSIC import app

MAX_SIZE_MB = 50
MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024


@app.on_message(filters.command("remove") & filters.reply)
async def remove_media(_, message: Message):
    replied = message.reply_to_message

    if not (replied and replied.video):
        return await message.reply_text("❌ 𝐏ʟᴇᴀꜱᴇ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ *𝐕ɪᴅᴇᴏ* 𝐌ᴇꜱꜱᴀɢᴇ.")
    if len(message.command) < 2:
        return await message.reply_text("ℹ️ 𝐔ꜱᴇ `/remove audio` ᴏʀ `/remove video`.", quote=True)

    if replied.video.file_size > MAX_SIZE_BYTES:
        return await message.reply_text(
            f"🚫 𝐅ɪʟᴇ ɪꜱ 𝐓ᴏᴏ 𝐋ᴀʀɢᴇ ({replied.video.file_size // (1024*1024)} 𝐌𝐁).\n"
            f"𝐌ᴀxɪᴍᴜᴍ 𝐀ʟʟᴏᴡᴇᴅ 𝐒ɪᴢᴇ ɪꜱ {MAX_SIZE_MB} 𝐌𝐁."
        )

    command = message.command[1].lower()
    processing_msg = await message.reply_text("🔧 𝐏ʀᴏᴄᴇꜱꜱɪɴɢ 𝐕ɪᴅᴇᴏ…")

    file_path = None
    try:
        file_path = await replied.download(file_name="media_input.mp4")

        if command == "audio":
            output_audio = "output_audio.mp3"

            def process_audio():
                audio = AudioSegment.from_file(file_path)
                audio = audio.set_channels(1)
                audio.export(output_audio, format="mp3")

            await asyncio.to_thread(process_audio)
            await app.send_audio(message.chat.id, output_audio, caption="🎧 𝐀ᴜᴅɪᴏ 𝐄xᴛʀᴀᴄᴛᴇᴅ.")
            os.remove(output_audio)

        elif command == "video":
            output_video = "output_video.mp4"

            def process_video():
                os.system(f"ffmpeg -hide_banner -loglevel error -i '{file_path}' -c copy -an '{output_video}'")

            await asyncio.to_thread(process_video)
            await app.send_video(message.chat.id, output_video, caption="🎞️ 𝐕ɪᴅᴇᴏ ᴡɪᴛʜ 𝐍ᴏ 𝐀ᴜᴅɪᴏ.")
            os.remove(output_video)

        else:
            return await message.reply_text("❌ 𝐈ɴᴠᴀʟɪᴅ 𝐂ᴏᴍᴍᴀɴᴅ. 𝐔ꜱᴇ `/remove audio` ᴏʀ `/remove video`.")

    except Exception as e:
        await message.reply_text(f"❌ 𝐄ʀʀᴏʀ: {e}")

    finally:
        await processing_msg.delete()
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
