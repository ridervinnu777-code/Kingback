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
from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from AZURAMUSIC.utils.Azura_ban import admin_filter
from AZURAMUSIC import app

# ── KripanshEmojis_by_fStikBot pack IDs ──
_KE_DEL   = 6129486856212979482   # 🗑️
_KE_WARN  = 6129782440157256336   # ⚠️
_KE_OK    = 6129812419028982717   # ✅
_KE_FIRE  = 6129792056589031358   # 🔥
_KE_SKULL = 6132184924603554220   # 💀

def ke(eid, fb):
    return f'<emoji id={eid}>{fb}</emoji>'


@app.on_message(filters.command("purge") & admin_filter)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴀ 𝐁ᴀꜱɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**𝐈 𝐂ᴀɴ'ᴛ 𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐌ᴇꜱꜱᴀɢᴇꜱ. 𝐓ʜᴇ 𝐌ᴇꜱꜱᴀɢᴇꜱ 𝐌ᴀʏ ʙᴇ 𝐓ᴏᴏ 𝐎ʟᴅ, 𝐈 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐇ᴀᴠᴇ 𝐃ᴇʟᴇᴛᴇ 𝐑ɪɢʜᴛꜱ, ᴏʀ 𝐓ʜɪꜱ 𝐌ɪɢʜᴛ 𝐍ᴏᴛ ʙᴇ ᴀ 𝐒ᴜᴘᴇʀɢʀᴏᴜᴘ.**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**𝐒ᴏᴍᴇ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ, 𝐑ᴇᴘᴏʀᴛ ɪᴛ 𝐔ꜱɪɴɢ** `/bug`<b>𝐄ʀʀᴏʀ:</b> <code>{ef}</code>")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(
            f"{ke(_KE_OK,'✅')} {ke(_KE_DEL,'🗑️')} <b>𝐃ᴇʟᴇᴛᴇᴅ</b> <code>{count_del_msg}</code> <b>𝐌ᴇꜱꜱᴀɢᴇꜱ</b> {ke(_KE_FIRE,'🔥')}"
        )
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text(f"{ke(_KE_WARN,'⚠️')} <b>𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐒ᴛᴀʀᴛ 𝐏ᴜʀɢᴇ !</b>")
    return





@app.on_message(filters.command("spurge") & admin_filter)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴀ 𝐁ᴀꜱɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**𝐈 𝐂ᴀɴ'ᴛ 𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐌ᴇꜱꜱᴀɢᴇꜱ. 𝐓ʜᴇ 𝐌ᴇꜱꜱᴀɢᴇꜱ 𝐌ᴀʏ ʙᴇ 𝐓ᴏᴏ 𝐎ʟᴅ, 𝐈 𝐌ɪɢʜᴛ 𝐍ᴏᴛ 𝐇ᴀᴠᴇ 𝐃ᴇʟᴇᴛᴇ 𝐑ɪɢʜᴛꜱ, ᴏʀ 𝐓ʜɪꜱ 𝐌ɪɢʜᴛ 𝐍ᴏᴛ ʙᴇ ᴀ 𝐒ᴜᴘᴇʀɢʀᴏᴜᴘ.**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**𝐒ᴏᴍᴇ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ, 𝐑ᴇᴘᴏʀᴛ ɪᴛ 𝐔ꜱɪɴɢ** `/bug`<b>𝐄ʀʀᴏʀ:</b> <code>{ef}</code>")           
            return        
    await msg.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐒ᴛᴀʀᴛ 𝐏ᴜʀɢᴇ !**")
    return


@app.on_message(filters.command("del") & admin_filter)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐂ᴀɴ'ᴛ 𝐏ᴜʀɢᴇ 𝐌ᴇꜱꜱᴀɢᴇꜱ ɪɴ ᴀ 𝐁ᴀꜱɪᴄ 𝐆ʀᴏᴜᴘ 𝐌ᴀᴋᴇ 𝐒ᴜᴘᴇʀ 𝐆ʀᴏᴜᴘ.**")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**𝐖ʜᴀᴛ 𝐃ᴏ 𝐘ᴏᴜ 𝐖ᴀɴᴛ ᴛᴏ 𝐃ᴇʟᴇᴛᴇ.**")
        return
