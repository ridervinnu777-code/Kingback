# -----------------------------------------------
# 🔴 Azura ✘ Music Project
# 🔷️ Developed & Maintained by: 𝐌ʀ 𝐕ɪɴɴᴜ
# 📅 Copyright © 2026 – All Rights Reserved
# -----------------------------------------------

import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from AZURAMUSIC import app
from AZURAMUSIC.utils.database import get_assistant
from config import OWNER_ID


OWNER_ID = int(OWNER_ID)


@app.on_message(
    filters.command("gadd")
    & filters.user(OWNER_ID)
)
async def add_allbot(client, message: Message):

    if len(message.command) != 2:
        return await message.reply(
            "**✦ 𝐈ɴᴠᴀʟɪᴅ 𝐂ᴏᴍᴍᴀɴᴅ 𝐅ᴏʀᴍᴀᴛ.**\n\n"
            "**𝐔ꜱᴇ:** `/gadd @Bot_username`"
        )

    bot_username = message.command[1].lstrip("@")

    try:
        userbot = await get_assistant(message.chat.id)

        bot = await app.get_users(bot_username)
        bot_id = bot.id

        progress = await message.reply(
            f"✦ **𝐀ᴅᴅɪɴɢ @{bot_username} 𝐈ɴ 𝐀ʟʟ 𝐂ʜᴀᴛꜱ...**"
        )

        done = 0
        failed = 0

        async for dialog in userbot.get_dialogs():

            chat_id = dialog.chat.id

            # Skip this specific chat
            if chat_id == -1003995146428:
                continue

            try:
                await userbot.add_chat_members(
                    chat_id,
                    bot_id
                )

                done += 1

            except FloodWait as e:
                await asyncio.sleep(e.value)
                failed += 1

            except Exception:
                failed += 1

            try:
                await progress.edit(
                    f"**✦ 𝐀ᴅᴅɪɴɢ @{bot_username}**\n\n"
                    f"**➥ 𝐀ᴅᴅᴇᴅ ɪɴ {done} 𝐂ʜᴀᴛꜱ ✔**\n"
                    f"**➥ 𝐅ᴀɪʟᴇᴅ ɪɴ {failed} 𝐂ʜᴀᴛꜱ ✘**"
                )
            except Exception:
                pass

            await asyncio.sleep(3)

        await progress.edit(
            f"**✦ @{bot_username} 𝐁ᴏᴛ 𝐀ᴅᴅɪɴɢ 𝐂ᴏᴍᴘʟᴇᴛᴇᴅ 🎉**\n\n"
            f"**➥ 𝐀ᴅᴅᴇᴅ ɪɴ {done} 𝐂ʜᴀᴛꜱ ✅**\n"
            f"**➥ 𝐅ᴀɪʟᴇᴅ ɪɴ {failed} 𝐂ʜᴀᴛꜱ ✘**"
        )

    except Exception:
        await message.reply(
            "❌ **𝐔ɴᴀʙʟᴇ ᴛᴏ 𝐏ʀᴏᴄᴇꜱꜱ ᴛʜᴇ 𝐑ᴇǫᴜᴇꜱᴛ.**"
        )
