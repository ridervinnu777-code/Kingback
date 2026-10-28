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
from AZURAMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🌚** ",
           " **➤ 𝐂ʜᴜᴘ 𝐂ʜᴀᴘ ꜱᴏ 𝐉ᴀ 🙊** ",
           " **➤ 𝐏ʜᴏɴᴇ 𝐑ᴀᴋʜ 𝐊ᴀʀ ꜱᴏ 𝐉ᴀ, 𝐍ᴀʜɪ ᴛᴏ 𝐁ʜᴏᴏᴛ 𝐀ᴀ 𝐉ᴀʏᴇɢᴀ..👻** ",
           " **➤ 𝐀ᴡᴇᴇ 𝐁ᴀʙᴜ 𝐒ᴏɴᴀ 𝐃ɪɴ 𝐌ᴇɪɴ 𝐊ᴀʀ 𝐋ᴇɴᴀ 𝐀ʙʜɪ ꜱᴏ 𝐉ᴀᴏ..?? 🥲** ",
           " **➤ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 𝐘ᴇ 𝐀ᴘɴᴇ 𝐆ꜰ 𝐒ᴇ 𝐁ᴀᴀᴛ 𝐊ʀ 𝐑ʜᴀ 𝐇 𝐑ᴀᴊᴀɪ 𝐌ᴇ 𝐆ʜᴜꜱ 𝐊ᴀʀ, ꜱᴏ 𝐍ᴀʜɪ 𝐑ᴀʜᴀ 😜** ",
           " **➤ 𝐏ᴀᴘᴀ 𝐘ᴇ 𝐃ᴇᴋʜᴏ 𝐀ᴘɴᴇ 𝐁ᴇᴛᴇ 𝐊ᴏ 𝐑ᴀᴀᴛ 𝐁ʜᴀʀ 𝐏ʜᴏɴᴇ 𝐂ʜᴀʟᴀ 𝐑ʜᴀ 𝐇ᴀɪ 🤭** ",
           " **➤ 𝐉ᴀɴᴜ 𝐀ᴀᴊ 𝐑ᴀᴀᴛ 𝐊ᴀ 𝐒ᴄᴇɴᴇ 𝐁ɴᴀ 𝐋ᴇ..?? 🌠** ",
           " **➤ 𝐆ɴ 𝐒ᴅ 𝐓ᴄ.. 🙂** ",
           " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴡᴇᴇᴛ 𝐃ʀᴇᴀᴍ 𝐓ᴀᴋᴇ 𝐂ᴀʀᴇ..?? ✨** ",
           " **➤ 𝐑ᴀᴀᴛ 𝐁ʜᴜᴛ 𝐇ᴏ 𝐆ʏɪ 𝐇ᴀɪ ꜱᴏ 𝐉ᴀᴏ, 𝐆ɴ..?? 🌌** ",
           " **➤ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 11 𝐁ᴀᴊɴᴇ 𝐖ᴀʟᴇ 𝐇ᴀɪ 𝐘ᴇ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐏ʜᴏɴᴇ 𝐂ʜᴀʟᴀ 𝐑ʜᴀ 𝐍ᴀʜɪ ꜱᴏ 𝐍ᴀʜɪ 𝐑ʜᴀ 🕦** ",
           " **➤ 𝐊ᴀʟ 𝐒ᴜʙʜᴀ 𝐒ᴄʜᴏᴏʟ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ, 𝐉ᴏ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐉ᴀɢ 𝐑ʜᴇ 𝐇ᴏ 🏫** ",
           " **➤ 𝐁ᴀʙᴜ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴅ 𝐓ᴄ..?? 😊** ",
           " **➤ 𝐀ᴀᴊ 𝐁ʜᴜᴛ 𝐓ʜᴀɴᴅ 𝐇ᴀɪ, 𝐀ᴀʀᴀᴍ 𝐒ᴇ 𝐉ᴀʟᴅɪ ꜱᴏ 𝐉ᴀᴛɪ 𝐇ᴏᴏɴ 🌼** ",
           " **➤ 𝐉ᴀɴᴇᴍᴀɴ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🌷** ",
           " **➤ 𝐌ᴇ 𝐉ᴀ 𝐑ᴀʜɪ 𝐒ᴏɴᴇ, 𝐆ɴ 𝐒ᴅ 𝐓ᴄ 🏵️** ",
           " **➤ 𝐇ᴇʟʟᴏ 𝐉ɪ 𝐍ᴀᴍᴀꜱᴛᴇ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 🍃** ",
           " **➤ 𝐇ᴇʏ, 𝐁ᴀʙʏ 𝐊ᴋʀʜ..? 𝐒ᴏɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ ☃️** ",
           " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐉ɪ, 𝐁ʜᴜᴛ 𝐑ᴀᴀᴛ 𝐇ᴏ 𝐆ʏɪ..? ⛄** ",
           " **➤ 𝐌ᴇ 𝐉ᴀ 𝐑ᴀʜɪ 𝐑ᴏɴᴇ, 𝐈 𝐌ᴇᴀɴ 𝐒ᴏɴᴇ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐉ɪ 😁** ",
           " **➤ 𝐌ᴀᴄʜʜᴀʟɪ 𝐊ᴏ 𝐊ᴇʜᴛᴇ 𝐇ᴀɪ 𝐅ɪꜱʜ, 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐃ᴇᴀʀ 𝐌ᴀᴛ 𝐊ʀɴᴀ 𝐌ɪꜱꜱ, 𝐉ᴀ 𝐑ʜɪ 𝐒ᴏɴᴇ 🌄** ",
           " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐁ʀɪɢʜᴛꜰᴜʟʟ 𝐍ɪɢʜᴛ 🤭** ",
           " **➤ 𝐓ʜᴇ 𝐍ɪɢʜᴛ 𝐇ᴀꜱ 𝐅ᴀʟʟᴇɴ, ᴛʜᴇ 𝐃ᴀʏ ɪꜱ 𝐃ᴏɴᴇ,, ᴛʜᴇ 𝐌ᴏᴏɴ 𝐇ᴀꜱ 𝐓ᴀᴋᴇɴ ᴛʜᴇ 𝐏ʟᴀᴄᴇ ᴏꜰ ᴛʜᴇ 𝐒ᴜɴ... 😊** ",
           " **➤ 𝐌ᴀʏ 𝐀ʟʟ 𝐘ᴏᴜʀ 𝐃ʀᴇᴀᴍꜱ 𝐂ᴏᴍᴇ 𝐓ʀᴜᴇ ❤️** ",
           " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐒ᴘʀɪɴᴋʟᴇꜱ 𝐒ᴡᴇᴇᴛ 𝐃ʀᴇᴀᴍ 💚** ",
           " **➤ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ, 𝐍ɪɴᴅ 𝐀ᴀ 𝐑ʜɪ 𝐇ᴀɪ 🥱** ",
           " **➤ 𝐃ᴇᴀʀ 𝐅ʀɪᴇɴᴅ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 💤** ",
           " **➤ 𝐁ᴀʙʏ 𝐀ᴀᴊ 𝐑ᴀᴀᴛ 𝐊ᴀ 𝐒ᴄᴇɴᴇ 𝐁ɴᴀ 𝐋ᴇ 🥰** ",
           " **➤ 𝐈ᴛɴɪ 𝐑ᴀᴀᴛ 𝐌ᴇ 𝐉ᴀɢ 𝐊ᴀʀ 𝐊ʏᴀ 𝐊ᴀʀ 𝐑ʜᴇ 𝐇ᴏ 𝐒ᴏɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ 😜** ",
           " **➤ 𝐂ʟᴏꜱᴇ 𝐘ᴏᴜʀ 𝐄ʏᴇꜱ 𝐒ɴᴜɢɢʟᴇ 𝐔ᴘ 𝐓ɪɢʜᴛ,, ᴀɴᴅ 𝐑ᴇᴍᴇᴍʙᴇʀ 𝐓ʜᴀᴛ 𝐀ɴɢᴇʟꜱ, 𝐖ɪʟʟ 𝐖ᴀᴛᴄʜ 𝐎ᴠᴇʀ 𝐘ᴏᴜ 𝐓ᴏɴɪɢʜᴛ... 💫** ",
           ]

VC_TAG = [ "**➤ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐊ᴇꜱᴇ 𝐇ᴏ 🐱**",
         "**➤ 𝐆ᴍ, 𝐒ᴜʙʜᴀ 𝐇ᴏ 𝐆ʏɪ 𝐔ᴛʜɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ 🌤️**",
         "**➤ 𝐆ᴍ 𝐁ᴀʙʏ, 𝐂ʜᴀɪ 𝐏ɪ 𝐋ᴏ ☕**",
         "**➤ 𝐉ᴀʟᴅɪ 𝐔ᴛʜᴏ, 𝐒ᴄʜᴏᴏʟ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ 🏫**",
         "**➤ 𝐆ᴍ, 𝐂ʜᴜᴘ 𝐂ʜᴀᴘ 𝐁ɪꜱᴛᴇʀ 𝐒ᴇ 𝐔ᴛʜᴏ 𝐕ʀɴᴀ 𝐏ᴀɴɪ 𝐃ᴀʟ 𝐃ᴜɴɢɪ 🧊**",
         "**➤ 𝐁ᴀʙʏ 𝐔ᴛʜᴏ 𝐀ᴜʀ 𝐉ᴀʟᴅɪ 𝐅ʀᴇꜱʜ 𝐇ᴏ 𝐉ᴀᴏ, 𝐍ᴀꜱᴛᴀ 𝐑ᴇᴀᴅʏ 𝐇ᴀɪ 🫕**",
         "**➤ 𝐎ꜰꜰɪᴄᴇ 𝐍ᴀʜɪ 𝐉ᴀɴᴀ 𝐊ʏᴀ 𝐉ɪ 𝐀ᴀᴊ, 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐔ᴛʜᴇ 𝐍ᴀʜɪ 🏣**",
         "**➤ 𝐆ᴍ 𝐃ᴏꜱᴛ, 𝐂ᴏꜰꜰᴇᴇ/𝐓ᴇᴀ 𝐊ʏᴀ 𝐋ᴏɢᴇ ☕🍵**",
         "**➤ 𝐁ᴀʙʏ 8 𝐁ᴀᴊɴᴇ 𝐖ᴀʟᴇ 𝐇ᴀɪ, 𝐀ᴜʀ 𝐓ᴜᴍ 𝐀ʙʜɪ 𝐓ᴋ 𝐔ᴛʜᴇ 𝐍ᴀʜɪ 🕖**",
         "**➤ 𝐊ʜᴜᴍʙʜᴋᴀʀᴀɴ 𝐊ɪ 𝐀ᴜʟᴀᴅ 𝐔ᴛʜ 𝐉ᴀᴀ... ☃️**",
         "**➤ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐇ᴀᴠᴇ ᴀ 𝐍ɪᴄᴇ 𝐃ᴀʏ... 🌄**",
         "**➤ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐇ᴀᴠᴇ ᴀ 𝐆ᴏᴏᴅ 𝐃ᴀʏ... 🪴**",
         "**➤ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐇ᴏᴡ ᴀʀᴇ 𝐘ᴏᴜ 𝐁ᴀʙʏ 😇**",
         "**➤ 𝐌ᴜᴍᴍʏ 𝐃ᴇᴋʜᴏ 𝐘ᴇ 𝐍ᴀʟᴀʏᴋ 𝐀ʙʜɪ 𝐓ᴀᴋ ꜱᴏ 𝐑ʜᴀ 𝐇ᴀɪ... 😵‍💫**",
         "**➤ 𝐑ᴀᴀᴛ 𝐁ʜᴀʀ 𝐁ᴀʙᴜ 𝐒ᴏɴᴀ 𝐊ʀ 𝐑ʜᴇ ᴛʜᴇ 𝐊ʏᴀ, 𝐉ᴏ 𝐀ʙʜɪ 𝐓ᴋ ꜱᴏ 𝐑ʜᴇ 𝐇ᴏ 𝐔ᴛʜɴᴀ 𝐍ᴀʜɪ 𝐇ᴀɪ 𝐊ʏᴀ... 😏**",
         "**➤ 𝐁ᴀʙᴜ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐔ᴛʜ 𝐉ᴀᴏ 𝐀ᴜʀ 𝐆ʀᴏᴜᴘ 𝐌ᴇ 𝐒ᴀʙ 𝐅ʀɪᴇɴᴅꜱ 𝐊ᴏ 𝐆ᴍ 𝐖ɪꜱʜ 𝐊ʀᴏ... 🌟**",
         "**➤ 𝐏ᴀᴘᴀ 𝐘ᴇ 𝐀ʙʜɪ 𝐓ᴀᴋ 𝐔ᴛʜ 𝐍ᴀʜɪ, 𝐒ᴄʜᴏᴏʟ 𝐊ᴀ 𝐓ɪᴍᴇ 𝐍ɪᴋᴀʟᴛᴀ 𝐉ᴀ 𝐑ʜᴀ 𝐇ᴀɪ... 🥲**",
         "**➤ 𝐉ᴀɴᴇᴍᴀɴ 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ, 𝐊ʏᴀ 𝐊ʀ 𝐑ʜᴇ 𝐇ᴏ ... 😅**",
         "**➤ 𝐆ᴍ 𝐁ᴇᴀꜱᴛɪᴇ, 𝐁ʀᴇᴀᴋꜰᴀꜱᴛ 𝐇ᴜᴀ 𝐊ʏᴀ... 🍳**",
        ]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐎ɴʟʏ ꜰᴏʀ 𝐆ʀᴏᴜᴘꜱ.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ 𝐘ᴏᴜ ᴀʀᴇ 𝐍ᴏᴛ 𝐀ᴅᴍɪɴ 𝐁ᴀʙʏ, 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐓ᴀɢ 𝐌ᴇᴍʙᴇʀꜱ. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐓ʏᴘᴇ 𝐋ɪᴋᴇ 𝐓ʜɪꜱ / 𝐑ᴇᴘʟʏ 𝐀ɴʏ 𝐌ᴇꜱꜱᴀɢᴇ 𝐍ᴇxᴛ 𝐓ɪᴍᴇ 𝐁ᴏᴛ 𝐓ᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐓ʏᴘᴇ 𝐋ɪᴋᴇ 𝐓ʜɪꜱ / 𝐑ᴇᴘʟʏ 𝐀ɴʏ 𝐌ᴇꜱꜱᴀɢᴇ 𝐍ᴇxᴛ 𝐓ɪᴍᴇ 𝐅ᴏᴛ 𝐓ᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall 𝐆ᴏᴏᴅ 𝐌ᴏʀɴɪɴɢ 𝐓ʏᴘᴇ 𝐋ɪᴋᴇ 𝐓ʜɪꜱ / 𝐑ᴇᴘʟʏ 𝐀ɴʏ 𝐌ᴇꜱꜱᴀɢᴇ 𝐍ᴇxᴛ 𝐓ɪᴍᴇ 𝐁ᴏᴛ 𝐓ᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ 𝐏ʟᴇᴀꜱᴇ ᴀᴛ 𝐅ɪʀꜱᴛ 𝐒ᴛᴏᴘ 𝐑ᴜɴɴɪɴɢ 𝐌ᴇɴᴛɪᴏɴ 𝐏ʀᴏᴄᴇꜱꜱ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](𝐓𝐆://𝐔ꜱᴇʀ?𝐈𝐃={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐎ɴʟʏ ꜰᴏʀ 𝐆ʀᴏᴜᴘꜱ.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ 𝐘ᴏᴜ ᴀʀᴇ 𝐍ᴏᴛ 𝐀ᴅᴍɪɴ 𝐁ᴀʙʏ, 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐓ᴀɢ 𝐌ᴇᴍʙᴇʀꜱ. ")
    if chat_id in spam_chats:
        return await message.reply("๏ 𝐏ʟᴇᴀꜱᴇ ᴀᴛ 𝐅ɪʀꜱᴛ 𝐒ᴛᴏᴘ 𝐑ᴜɴɴɪɴɢ 𝐌ᴇɴᴛɪᴏɴ 𝐏ʀᴏᴄᴇꜱꜱ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐈'ᴍ 𝐍ᴏᴛ 𝐓ᴀɢɢɪɴɢ 𝐁ᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ 𝐘ᴏᴜ ᴀʀᴇ 𝐍ᴏᴛ 𝐀ᴅᴍɪɴ 𝐁ᴀʙʏ, 𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐓ᴀɢ 𝐌ᴇᴍʙᴇʀꜱ.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ 𝐌ᴇɴᴛɪᴏɴ 𝐏ʀᴏᴄᴇꜱꜱ 𝐒ᴛᴏᴘᴘᴇᴅ ๏")


