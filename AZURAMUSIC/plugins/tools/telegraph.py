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
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AZURAMUSIC import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"𝐄ʀʀᴏʀ: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "✦ 𝐏ʟᴇᴀꜱᴇ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇᴅɪᴀ ᴛᴏ 𝐔ᴘʟᴏᴀᴅ ᴏɴ 𝐓ᴇʟᴇɢʀᴀᴘʜ"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐌ᴇᴅɪᴀ 𝐅ɪʟᴇ 𝐔ɴᴅᴇʀ 200𝐌𝐁.")

    try:
        text = await message.reply("✦ 𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...")

        async def progress(current, total):
            try:
                await text.edit_text(f"✦ 𝐃ᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("✦ 𝐔ᴘʟᴏᴀᴅɪɴɢ ᴛᴏ 𝐓ᴇʟᴇɢʀᴀᴘʜ...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"✦ | [𝐓ᴀᴘ ᴛʜᴇ 𝐋ɪɴᴋ]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "𝐓ᴀᴘ 𝐇ᴇʀᴇ ᴛᴏ 𝐒ᴇᴇ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"✦ 𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ 𝐖ʜɪʟᴇ 𝐔ᴘʟᴏᴀᴅɪɴɢ 𝐘ᴏᴜʀ 𝐅ɪʟᴇ\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"✦ 𝐅ɪʟᴇ 𝐔ᴘʟᴏᴀᴅ 𝐅ᴀɪʟᴇᴅ\n\n✦ <i>𝐑ᴇᴀꜱᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass
