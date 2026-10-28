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
import requests
from pyrogram import filters
from pyrogram.types import Message
from AZURAMUSIC import app


@app.on_message(filters.command("waifu"))
async def waifu_command_handler(_, message: Message):
    try:
        args = message.text.split(maxsplit=1)
        tag = args[1] if len(args) > 1 else "maid"

        waifu_data = get_waifu_data(tag)

        if waifu_data and 'images' in waifu_data and waifu_data['images']:
            image = waifu_data['images'][0]
            await message.reply_photo(
                photo=image["url"],
                caption=f"🌸 𝐇ᴇʀᴇ'ꜱ 𝐘ᴏᴜʀ 𝐖ᴀɪꜰᴜ ({tag})"
            )
        else:
            await message.reply_text("❌ 𝐍ᴏ 𝐖ᴀɪꜰᴜꜱ 𝐅ᴏᴜɴᴅ ᴡɪᴛʜ 𝐓ʜᴀᴛ 𝐓ᴀɢ.")

    except Exception as e:
        await message.reply_text(f"⚠️ 𝐄ʀʀᴏʀ: `{str(e)}`")


def get_waifu_data(tag):
    try:
        response = requests.get(
            "https://api.waifu.im/search",
            params={
                "included_tags": tag,
                "height": ">=2000"
            }
        )
        if response.status_code == 200:
            return response.json()
    except:
        return None
