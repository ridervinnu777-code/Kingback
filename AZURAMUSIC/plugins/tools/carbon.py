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
import aiohttp
from io import BytesIO
from AZURAMUSIC import app
from pyrogram import filters

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐓ᴇxᴛ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐌ᴀᴋᴇ ᴀ 𝐂ᴀʀʙᴏɴ.**")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐓ᴇxᴛ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐌ᴀᴋᴇ ᴀ 𝐂ᴀʀʙᴏɴ.**")
    text = await message.reply("𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("**𝐔ᴘʟᴏᴀᴅɪɴɢ...**")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()


