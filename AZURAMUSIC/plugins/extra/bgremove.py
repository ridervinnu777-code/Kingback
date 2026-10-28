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
import aiohttp
import aiofiles
from aiohttp import ContentTypeError
from AZURAMUSIC import app as app
from pyrogram import filters

def check_filename(filroid):
    if os.path.exists(filroid):
        no = 1
        while True:
            ult = "{0}_{2}{1}".format(*os.path.splitext(filroid) + (no,))
            if os.path.exists(ult):
                no += 1
            else:
                return ult
    return filroid

async def RemoveBG(input_file_name):
    headers = {"X-API-Key": "P6oDw1YNnMdkoMXxmWJinHQK"}
    files = {"image_file": open(input_file_name, "rb").read()}
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            "https://api.remove.bg/v1.0/removebg", headers=headers, data=files
        ) as y:
            contentType = y.headers.get("content-type")
            if "image" not in contentType:
                return False, (await y.json())

            name = check_filename("alpha.png")
            file = await aiofiles.open(name, "wb")
            await file.write(await y.read())
            await file.close()
            return True, name


@app.on_message(filters.command("rmbg"))
async def rmbg(bot, message):
  rmbg = await message.reply("𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...") 
  replied = message.reply_to_message
  if not replied:
      return await rmbg.edit("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐏ʜᴏᴛᴏ ᴛᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐈ᴛ'ꜱ 𝐁ᴀᴄᴋɢʀᴏᴜᴅ")

  if replied.photo:
      photo = await bot.download_media(replied)
      x, y = await RemoveBG(photo)
      os.remove(photo)
      if not x:
          bruh = y["errors"][0]
          details = bruh.get("detail", "")
          return await rmbg.edit(f"𝐄𝐑𝐑𝐎𝐑 ~ {bruh['title']},\n{details}")
      await message.reply_photo(photo=y,caption="𝐇ᴇʀᴇ ɪꜱ 𝐘ᴏᴜʀ 𝐈ᴍᴀɢᴇ 𝐖ɪᴛʜᴏᴜᴛ 𝐁ᴀᴄᴋɢʀᴏᴜɴᴅ")
      await message.reply_document(document=y)
      await rmbg.delete()
      return os.remove(y)
  await rmbg.edit("𝐑ᴇᴘʟʏ 𝐎ɴʟʏ ᴛᴏ ᴀ 𝐏ʜᴏᴛᴏ ᴛᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐈ᴛ'ꜱ 𝐁ᴀᴄᴋɢʀᴏᴜɴᴅ")
