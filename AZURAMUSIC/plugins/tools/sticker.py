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
import base64
import httpx
import os
from pyrogram import filters
from config import BOT_USERNAME
from AZURAMUSIC import app
from pyrogram import filters
import pyrogram
from uuid import uuid4
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


######### sticker id

@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"𝐄ʀʀᴏʀ: {e}")
    else:
        message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴀ 𝐒ᴛɪᴄᴋᴇʀ 𝐈𝐃 𝐀ꜰᴛᴇʀ /st 𝐂ᴏᴍᴍᴀɴᴅ.")


#---------





@app.on_message(filters.command("packkang"))
async def _packkang(app :app,message):  
    txt = await message.reply_text("**𝐏ʀᴏᴄᴇꜱꜱɪɴɢ....**")
    if not message.reply_to_message:
        await txt.edit('𝐑ᴇᴘʟʏ ᴛᴏ 𝐌ᴇꜱꜱᴀɢᴇ')
        return
    if not message.reply_to_message.sticker:
        await txt.edit('𝐑ᴇᴘʟʏ ᴛᴏ 𝐒ᴛɪᴄᴋᴇʀ')
        return
    if message.reply_to_message.sticker.is_animated or  message.reply_to_message.sticker.is_video:
        return await txt.edit("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐍ᴏɴ-𝐀ɴɪᴍᴀᴛᴇᴅ 𝐒ᴛɪᴄᴋᴇʀ")
    if len(message.command) < 2:
        pack_name =  f'{message.from_user.first_name}_sticker_pack_by_@{BOT_USERNAME}'
    else :
        pack_name = message.text.split(maxsplit=1)[1]
    short_name = message.reply_to_message.sticker.set_name
    stickers = await app.invoke(
        pyrogram.raw.functions.messages.GetStickerSet(
            stickerset=pyrogram.raw.types.InputStickerSetShortName(
                short_name=short_name),
            hash=0))
    shits = stickers.documents
    sticks = []
    
    for i in shits:
        sex = pyrogram.raw.types.InputDocument(
                id=i.id,
                access_hash=i.access_hash,
                file_reference=i.thumbs[0].bytes
            )
        
        sticks.append(
            pyrogram.raw.types.InputStickerSetItem(
                document=sex,
                emoji=i.attributes[1].alt
            )
        )

    try:
        short_name = f'stikcer_pack_{str(uuid4()).replace("-","")}_by_{app.me.username}'
        user_id = await app.resolve_peer(message.from_user.id)
        await app.invoke(
            pyrogram.raw.functions.stickers.CreateStickerSet(
                user_id=user_id,
                title=pack_name,
                short_name=short_name,
                stickers=sticks,
            )
        )
        await txt.edit(f"**𝐇ᴇʀᴇ ɪꜱ 𝐘ᴏᴜʀ 𝐊ᴀɴɢᴇᴅ 𝐋ɪɴᴋ**!\n**𝐓ᴏᴛᴀʟ 𝐒ᴛɪᴄᴋᴇʀ **: {len(sticks)}",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝐏ᴀᴄᴋ 𝐋ɪɴᴋ",url=f"http://t.me/addstickers/{short_name}")]]))
    except Exception as e:
        await message.reply(str(e))


###### sticker id =
@app.on_message(filters.command(["stickerid","stid"]))
async def sticker_id(app: app, msg):
    if not msg.reply_to_message:
        await msg.reply_text("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐒ᴛɪᴄᴋᴇʀ")        
    elif not msg.reply_to_message.sticker:
        await msg.reply_text("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐒ᴛɪᴄᴋᴇʀ")        
    st_in = msg.reply_to_message.sticker
    await msg.reply_text(f"""
⊹ <u>**𝐒ᴛɪᴄᴋᴇʀ 𝐈ɴꜰᴏ**</u> ⊹
**⊚ 𝐒ᴛɪᴄᴋᴇʀ 𝐈𝐃 **: `{st_in.file_id}`\n
**⊚ sᴛɪᴄᴋᴇʀ ᴜɴɪǫᴜᴇ ɪᴅ **: `{st_in.file_unique_id}`
""")


#####
