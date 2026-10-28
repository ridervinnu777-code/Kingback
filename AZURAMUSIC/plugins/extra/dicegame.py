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
from pyrogram import Client, enums, filters
import asyncio
from AZURAMUSIC import app as app
from pyrogram.handlers import MessageHandler


@app.on_message(filters.command("dice"))
async def dice(bot, message):
    x=await bot.send_dice(message.chat.id)
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)
  
@app.on_message(filters.command("dart"))
async def dart(bot, message):
    x=await bot.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)

@app.on_message(filters.command("basket"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🏀")
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)
@app.on_message(filters.command("jackpot"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎰")
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)
@app.on_message(filters.command("ball"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "🎳")
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)
@app.on_message(filters.command("football"))
async def basket(bot, message):
    x=await bot.send_dice(message.chat.id, "⚽")
    m=x.dice.value
    await message.reply_text(f"𝐇ᴇʏ {message.from_user.mention} 𝐘ᴏᴜʀ 𝐒ᴄᴏʀᴇ ɪꜱ : {m}",quote=True)
__help__ = """
 Play Game With Emojis:
/dice - Dice 🎲
/dart - Dart 🎯
/basket - Basket Ball 🏀
/ball - Bowling Ball 🎳
/football - Football ⚽
/jackpot - Spin slot machine 🎰
 """

__mod_name__ = "𝐃ɪᴄᴇ"
