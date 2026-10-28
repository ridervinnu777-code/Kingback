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
from pyrogram import filters
import asyncio
import pyfiglet 
from random import choice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.handlers import MessageHandler
from AZURAMUSIC import app
def figle(text):
    x = pyfiglet.FigletFont.getFonts()
    font = choice(x)
    figled = str(pyfiglet.figlet_format(text,font=font))
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐂ʜᴀɴɢᴇ", callback_data="figlet"),InlineKeyboardButton(text="𝐂ʟᴏꜱᴇ", callback_data="close_reply")]])
    return figled, keyboard

@app.on_message(filters.command("figlet"))
async def echo(bot, message):
    global text
    try:
        text = message.text.split(' ',1)[1]
    except IndexError:
        return await message.reply_text("𝐄xᴀᴍᴘʟᴇ:\n\n`/figlet SHIVANSH PAPA `")
    kul_text, keyboard = figle(text)
    await message.reply_text(f"𝐇ᴇʀᴇ ɪꜱ 𝐘ᴏᴜʀ 𝐅ɪɢʟᴇᴛ :\n<pre>{kul_text}</pre>", quote=True, reply_markup=keyboard)

@app.on_callback_query(filters.regex("figlet"))
async def figlet_handler(Client, query: CallbackQuery):
  try:
      kul_text, keyboard = figle(text)
      await query.message.edit_text(f"𝐇ᴇʀᴇ ɪꜱ 𝐘ᴏᴜʀ 𝐅ɪɢʟᴇᴛ :\n<pre>{kul_text}</pre>", reply_markup=keyboard)
  except Exception as e : 
      await message.reply(e)
__mod_name__ = "𝐅ɪɢʟᴇᴛ" 
__help__="""
✦ /figlet*:* 𝐌ᴀᴋᴇꜱ 𝐅ɪɢʟᴇᴛ ᴏꜰ ᴛʜᴇ 𝐆ɪᴠᴇɴ 𝐓ᴇxᴛ
𝐄xᴀᴍᴘʟᴇ:\n\n`/figlet VINCENZO PAPA `"""
