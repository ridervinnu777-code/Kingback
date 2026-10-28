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
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.raw.functions.messages import DeleteHistory
from AZURAMUSIC import userbot as us, app
from AZURAMUSIC.core.userbot import assistants

@app.on_message(filters.command("sg"))
async def sg(client: Client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply("➤ 𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐔ꜱᴇʀ 𝐈𝐃/𝐔ꜱᴇʀɴᴀᴍᴇ ᴏʀ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐔ꜱᴇʀ.")

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    else:
        user_id = message.text.split()[1]

    loading = await message.reply("🔍 𝐒ᴇᴀʀᴄʜɪɴɢ...")

    try:
        user = await client.get_users(user_id)
    except Exception:
        return await loading.edit("✘ 𝐈ɴᴠᴀʟɪᴅ 𝐔ꜱᴇʀ. 𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐕ᴀʟɪᴅ 𝐈𝐃/𝐔ꜱᴇʀɴᴀᴍᴇ.")

    sangmata_bots = ["sangmata_bot", "sangmata_beta_bot"]
    target_bot = random.choice(sangmata_bots)

    if 1 in assistants:
        ubot = us.one
    else:
        return await loading.edit("✘ 𝐍ᴏ 𝐀ꜱꜱɪꜱᴛᴀɴᴛ 𝐔ꜱᴇʀʙᴏᴛ 𝐀ᴠᴀɪʟᴀʙʟᴇ.")

    try:
        sent = await ubot.send_message(target_bot, str(user.id))
        await sent.delete()
    except Exception as e:
        return await loading.edit(f"✘ 𝐄ʀʀᴏʀ: {e}")

    await asyncio.sleep(2)

    found = False
    async for msg in ubot.search_messages(target_bot):
        if not msg.text:
            continue
        await message.reply(
            f"🧾 <b>𝐇ɪꜱᴛᴏʀʏ:</b>\n\n{msg.text}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝐂ʟᴏꜱᴇ", callback_data="close")]])
        )
        found = True
        break

    if not found:
        await message.reply("✘ 𝐍ᴏ 𝐑ᴇꜱᴘᴏɴꜱᴇ 𝐑ᴇᴄᴇɪᴠᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ 𝐒ᴀɴɢᴍᴀᴛᴀ 𝐁ᴏᴛ.")

    try:
        peer = await ubot.resolve_peer(target_bot)
        await ubot.send(DeleteHistory(peer=peer, max_id=0, revoke=True))
    except Exception:
        pass

    await loading.delete()
