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
from pyrogram.types import Message
from AZURAMUSIC import app
from AZURAMUSIC.misc import SUDOERS
from AZURAMUSIC.utils.database import add_gban_user, remove_gban_user
from AZURAMUSIC.utils.decorators.language import language
from AZURAMUSIC.utils.extraction import extract_user
from config import BANNED_USERS


@app.on_message(filters.command(["block"]) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in BANNED_USERS:
        return await message.reply_text(_["block_1"].format(user.mention))
    await add_gban_user(user.id)
    BANNED_USERS.add(user.id)
    await message.reply_text(_["block_2"].format(user.mention))


@app.on_message(filters.command(["unblock"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in BANNED_USERS:
        return await message.reply_text(_["block_3"].format(user.mention))
    await remove_gban_user(user.id)
    BANNED_USERS.remove(user.id)
    await message.reply_text(_["block_4"].format(user.mention))


@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)
