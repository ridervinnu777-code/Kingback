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
from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from AZURAMUSIC import app
from config import OWNER_ID
from pyrogram.types import Message
from AZURAMUSIC.utils.Azura_ban import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("pin") & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋꜱ 𝐎ɴʟʏ ᴏɴ 𝐆ʀᴏᴜᴘꜱ !**")
    elif not replied:
        await message.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐏ɪɴ ɪᴛ !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐏ɪɴɴᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇ!**\n\n**𝐂ʜᴀᴛ:** {chat_title}\n**𝐀ᴅᴍɪɴ:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 𝐕ɪᴇᴡꜱ 𝐌ᴇꜱꜱᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("pinned"))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**𝐍ᴏ 𝐏ɪɴɴᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇ 𝐅ᴏᴜɴᴅ**")
    try:        
        await message.reply_text("𝐇ᴇʀᴇ ɪꜱ ᴛʜᴇ 𝐋ᴀᴛᴇꜱᴛ 𝐏ɪɴɴᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇ",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="📝 𝐕ɪᴇᴡ 𝐌ᴇꜱꜱᴀɢᴇ",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("unpin") & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋꜱ 𝐎ɴʟʏ ᴏɴ 𝐆ʀᴏᴜᴘꜱ !**")
    elif not replied:
        await message.reply_text("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐔ɴᴘɪɴ ɪᴛ !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐔ɴᴘɪɴɴᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇ!**\n\n**𝐂ʜᴀᴛ:** {chat_title}\n**𝐀ᴅᴍɪɴ:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 𝐕ɪᴇᴡꜱ 𝐌ᴇꜱꜱᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("removephoto") & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**𝐏ʀᴏᴄᴇꜱꜱɪɴɢ....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋ ᴏɴ 𝐆ʀᴏᴜᴘꜱ !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐏ʀᴏꜰɪʟᴇ 𝐏ʜᴏᴛᴏ ꜰʀᴏᴍ 𝐆ʀᴏᴜᴘ !\n𝐁ʏ** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴏꜱᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐆ʀᴏᴜᴘ 𝐏ʜᴏᴛᴏ !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("setphoto")& admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ᴏɴ ɢʀᴏᴜᴘs !`") 
      elif not reply:
           await msg.edit("**𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐏ʜᴏᴛᴏ ᴏʀ 𝐃ᴏᴄᴜᴍᴇɴᴛ.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐍ᴇᴡ 𝐏ʀᴏꜰɪʟᴇ 𝐏ʜᴏᴛᴏ 𝐈ɴꜱᴇʀᴛ !\n𝐁ʏ** {}".format(message.from_user.mention))
             else:
                await msg.edit("**𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ʀᴏɴɢ 𝐇ᴀᴘᴘᴇɴᴇᴅ 𝐓ʀʏ 𝐀ɴᴏᴛʜᴇʀ 𝐏ʜᴏᴛᴏ !**")
     
          except:
              await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴏꜱᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐏ʜᴏᴛᴏ !**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("settitle")& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋ ᴏɴ 𝐆ʀᴏᴜᴘꜱ !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐍ᴀᴍᴇ 𝐈ɴꜱᴇʀᴛ !\n𝐁ʏ** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴏꜱᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ !**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐍ᴀᴍᴇ 𝐈ɴꜱᴇʀᴛ !\n𝐁ʏ** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴏꜱᴛ 𝐍ᴇᴇᴅ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ !**")
          

    else:
       await msg.edit("**𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐑ᴇᴘʟʏ ᴛᴏ 𝐓ᴇxᴛ ᴏʀ 𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐓ɪᴛʟᴇ **")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("setdiscription") & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**𝐏ʀᴏᴄᴇꜱꜱɪɴɢ...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ 𝐖ᴏʀᴋꜱ ᴏɴ 𝐆ʀᴏᴜᴘꜱ!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐃ɪꜱᴄʀɪᴘᴛɪᴏɴ 𝐈ɴꜱᴇʀᴛ!**\n𝐁ʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴜꜱᴛ 𝐇ᴀᴠᴇ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪꜱᴄʀɪᴘᴛɪᴏɴ!**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ 𝐃ɪꜱᴄʀɪᴘᴛɪᴏɴ 𝐈ɴꜱᴇʀᴛ!**\n𝐁ʏ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**𝐓ʜᴇ 𝐔ꜱᴇʀ 𝐌ᴜꜱᴛ 𝐇ᴀᴠᴇ 𝐂ʜᴀɴɢᴇ 𝐈ɴꜰᴏ 𝐀ᴅᴍɪɴ 𝐑ɪɢʜᴛꜱ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪꜱᴄʀɪᴘᴛɪᴏɴ!**")
    else:
        await msg.edit("**𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐑ᴇᴘʟʏ ᴛᴏ 𝐓ᴇxᴛ ᴏʀ 𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ ᴛᴏ 𝐂ʜᴀɴɢᴇ 𝐆ʀᴏᴜᴘ 𝐃ɪꜱᴄʀɪᴘᴛᴏɴ!**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("lg")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**𝐒ᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ 𝐇ɪʀᴏ !!.**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# --------------------------------------------------------------------------------- #


