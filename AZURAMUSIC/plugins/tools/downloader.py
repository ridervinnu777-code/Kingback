from pyrogram import filters
from pyrogram.types import Message
from AZURAMUSIC import app
import requests
import os

@app.on_message(filters.command("vid"))
async def video_downloader(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❌ 𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐕ɪᴅᴇᴏ 𝐔𝐑𝐋.\n\n𝐄xᴀᴍᴘʟᴇ:\n/vid 𝐀ɴʏ_𝐕ɪᴅᴇᴏ_𝐔𝐑𝐋")

    video_url = message.text.split(None, 1)[1]

    msg = await message.reply("🔍 𝐅ᴇᴛᴄʜɪɴɢ 𝐕ɪᴅᴇᴏ...")

    # Step 1: Call API
    payload = {
        "url": video_url,
        "token": "c99f113fab0762d216b4545e5c3d615eefb30f0975fe107caab629d17e51b52d"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 14)",
    }

    try:
        r = requests.post("https://allvideodownloader.cc/wp-json/aio-dl/video-data/", data=payload, headers=headers)
        data = r.json()

        if "medias" not in data or not data["medias"]:
            return await msg.edit("❌ 𝐍ᴏ 𝐃ᴏᴡɴʟᴏᴀᴅᴀʙʟᴇ 𝐕ɪᴅᴇᴏ 𝐅ᴏᴜɴᴅ.")

        # Step 2: Get best quality video URL
        best_video = sorted(data["medias"], key=lambda x: x.get("quality", ""), reverse=True)[0]
        video_link = best_video["url"]

        # Step 3: Download the video to temp file
        await msg.edit("⬇️ 𝐃ᴏᴡɴʟᴏᴀᴅɪɴɢ 𝐕ɪᴅᴇᴏ...")

        file_name = "video.mp4"
        with requests.get(video_link, stream=True) as v:
            with open(file_name, "wb") as f:
                for chunk in v.iter_content(chunk_size=8192):
                    f.write(chunk)

        # Step 4: Send video to user
        await app.send_video(
            chat_id=message.chat.id,
            video=file_name,
            caption=f"🎬 {data.get('title', 'Video')}\n\n✅ ",
            supports_streaming=True
        )

        await msg.delete()
        os.remove(file_name)

    except Exception as e:
        await msg.edit(f"❌ 𝐄ʀʀᴏʀ: {str(e)}")
