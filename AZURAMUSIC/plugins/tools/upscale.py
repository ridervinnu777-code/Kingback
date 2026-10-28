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
import base64
import httpx
import os
import config 
from config import BOT_USERNAME
from AZURAMUSIC import app
from pyrogram import Client, filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import aiofiles, aiohttp, requests

async def image_loader(image: str, link: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            if resp.status == 200:
                f = await aiofiles.open(image, mode="wb")
                await f.write(await resp.read())
                await f.close()
                return image
            return image

@app.on_message(filters.command("upscale", prefixes="/"))
async def upscale_image(client, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    if not replied:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀɴ 𝐈ᴍᴀɢᴇ ...")
    if not replied.photo:
        return await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀɴ 𝐈ᴍᴀɢᴇ ...")

    aux = await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐖ᴀɪᴛ ...")
    image = await replied.download()

    try:
        # Use the DeepAI API to upscale the image
        response = requests.post(
            "https://api.deepai.org/api/torch-srgan",
            files={
                'image': open(image, 'rb'),
            },
            headers={'api-key': 'bf9ee957-9fad-46f5-a403-3e96ca9004e4'}
        )
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        image_link = data.get("output_url")

        if image_link:
            downloaded_image = await image_loader(image, image_link)
            await aux.delete()
            return await message.reply_document(downloaded_image)
        else:
            await aux.edit_text("𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐆ᴇᴛ ᴛʜᴇ 𝐎ᴜᴛᴘᴜᴛ 𝐈ᴍᴀɢᴇ 𝐋ɪɴᴋ.")
    except requests.exceptions.RequestException as e:
        await aux.edit_text(f"𝐑ᴇǫᴜᴇꜱᴛ 𝐅ᴀɪʟᴇᴅ: {str(e)}")
    except Exception as e:
        await aux.edit_text(f"𝐀ɴ 𝐔ɴᴇxᴘᴇᴄᴛᴇᴅ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
