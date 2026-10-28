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
from pyrogram import filters,enums
from pyrogram.types import ChatPermissions 
from AZURAMUSIC.utils.Azura_ban import admin_filter

@app.on_message(filters.command("unmuteall") & admin_filter)
async def unmute_all(_,msg):
    chat_id=msg.chat.id   
    user_id=msg.from_user.id
    x = 0
    bot=await app.get_chat_member(chat_id,user_id)
    bot_permission=bot.privileges.can_restrict_members==True 
    if bot_permission:
        banned_users = []
        async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
            banned_users.append(m.user.id)       
            try:
                    await app.restrict_chat_member(chat_id,banned_users[x], ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_polls=True,can_add_web_page_previews=True,can_invite_users=True))
                    print(f"ᴜɴᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs {m.user.mention}")
                    x += 1
                                        
            except Exception as e:
                print(e)
    else:
        await msg.reply_text("𝐄ɪᴛʜᴇʀ 𝐈 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ ᴛʜᴇ 𝐑ɪɢʜᴛ ᴛᴏ 𝐑ᴇꜱᴛʀɪᴄᴛ 𝐔ꜱᴇʀꜱ ᴏʀ 𝐘ᴏᴜ ᴀʀᴇ 𝐍ᴏᴛ ɪɴ 𝐒ᴜᴅᴏ 𝐔ꜱᴇʀꜱ")
