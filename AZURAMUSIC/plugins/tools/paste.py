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
from asyncio import get_running_loop, sleep, TimeoutError
from functools import partial
from AZURAMUSIC import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiohttp import ClientSession
import re
import os
import socket
import aiofiles
import aiohttp
import asyncio
from io import BytesIO

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image
    
aiohttpsession = ClientSession()

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")

def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode("utf-8").strip("\n\x00")
        if not data:
            break
        return data
    s.close()

async def paste(content):
    loop = get_running_loop()
    link = await loop.run_in_executor(None, partial(_netcat, "ezup.dev", 9999, content))
    return link

async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with aiohttpsession.head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return status == 200
    return False

@app.on_message(filters.command("paste"))
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴡɪᴛʜ /paste**")

    m = await message.reply_text("**𝐏ᴀꜱᴛɪɴɢ 𝐏ʟꜱ 𝐖ᴀɪᴛ 10 𝐒ᴇᴄ....**")

    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("**𝐘ᴏᴜ 𝐂ᴀɴ 𝐎ɴʟʏ 𝐏ᴀꜱᴛᴇ 𝐅ɪʟᴇꜱ 𝐒ᴍᴀʟʟᴇʀ 𝐓ʜᴀɴ 1𝐌ʙ.**")
        if not pattern.search(document.mime_type):
            return await m.edit("**𝐎ɴʟʏ 𝐓ᴇxᴛ 𝐅ɪʟᴇꜱ 𝐂ᴀɴ ʙᴇ 𝐏ᴀꜱᴛᴇᴅ.**")

        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            lines = await f.readlines()

        os.remove(doc)

        total_lines = len(lines)
        current_line = 0
        page_number = 1

        while current_line < total_lines:
            end_line = min(current_line + 50, total_lines)
            content_chunk = "".join(lines[current_line:end_line])
            carbon = await make_carbon(content_chunk)

            await m.delete()
            text = await message.reply("**✍️𝐏ᴀꜱᴛᴇᴅ ᴏɴ 𝐂ᴀʀʙᴏɴ 𝐏ᴀɢᴇ !**")
            await asyncio.sleep(0.4)
            await text.edit("**𝐔ᴘʟᴏᴀᴅɪɴɢ 𝐔ɴᴅᴇʀ 5 𝐒ᴇᴄ.**")
            await asyncio.sleep(0.4)
            await text.edit("**𝐔ᴘʟᴏᴀᴅɪɴɢ 𝐔ɴᴅᴇʀ 5 𝐒ᴇᴄ....**")
            caption = f"🌸𝐓ʜɪꜱ ɪꜱ  {page_number} 𝐏ᴀɢᴇ - {current_line + 1} 𝐓ᴏ {end_line} 𝐋ɪɴᴇꜱ..\n 𝐒ᴇɴᴅɪɴɢ 𝐌ᴏʀᴇ 𝐋ɪɴᴇꜱ ɪꜰ 𝐇ᴀᴠᴇ ᴏɴ 𝐍ᴇxᴛ 𝐏ᴀɢᴇ 𝐏ʟᴇᴀꜱᴇ 𝐖ᴀɪᴛ..."
            await message.reply_photo(carbon, caption=caption)
            await text.delete()
            carbon.close()

            current_line = end_line
            page_number += 1
            await sleep(1)  # Optional: Add a sleep to avoid rate limiting or being blocked

    else:
        await m.edit("**𝐔ɴꜱᴜᴘᴘᴏʀᴛᴇᴅ 𝐅ɪʟᴇ 𝐓ʏᴘᴇ. 𝐎ɴʟʏ 𝐓ᴇxᴛ 𝐅ɪʟᴇꜱ 𝐂ᴀɴ ʙᴇ 𝐏ᴀꜱᴛᴇᴅ.**")
