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
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from AZURAMUSIC import app

@app.on_message(~filters.private & filters.command(["groupdata"]), group=2)
async def instatus(app, message):
    start_time = time.perf_counter()
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    count = await app.get_chat_members_count(message.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        sent_message = await message.reply_text("𝐆𝐄𝐓𝐓𝐈𝐍𝐆 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍...")
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        async for ban in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        async for member in app.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await sent_message.edit(f"""
**➖➖➖➖➖➖➖
➤ 𝐍𝐀𝐌𝐄 : {message.chat.title} ✅
➤ 𝐌𝐄𝐌𝐁𝐄𝐑𝐒 : [ {count} ]🫂
➖➖➖➖➖➖➖
➤ 𝐁𝐎𝐓𝐒 : {bot}💡
➤ 𝐙𝐎𝐌𝐁𝐈𝐄𝐒 : {deleted_acc}🧟
➤ 𝐁𝐀𝐍𝐍𝐄𝐃 : {banned}🚫
➤ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑𝐒 : {premium_acc}🎁
➖➖➖➖➖➖➖
𝐓𝐈𝐌𝐄 𝐓𝐀𝐊𝐄𝐍 : {timelog} 𝐒**""")
    else:
        sent_message = await message.reply_text("𝐎𝐍𝐋𝐘 𝐀𝐃𝐌𝐈𝐍𝐒 𝐂𝐀𝐍 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 !")
        await sleep(5)
        await sent_message.delete()
