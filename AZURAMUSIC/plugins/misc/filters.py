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
import re
from AZURAMUSIC import app
from config import BOT_USERNAME
from AZURAMUSIC.utils.Azura_ban import admin_filter
from AZURAMUSIC.mongo.filtersdb import *
from AZURAMUSIC.utils.filters_func import GetFIlterMessage, get_text_reason, SendFilterMessage
from AZURAMUSIC.utils.shivdb import user_admin
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.command("filter") & admin_filter)
@user_admin
async def _filter(client, message):
    if not message.from_user:
        return
    
    chat_id = message.chat.id 
    if (
        message.reply_to_message
        and not len(message.command) == 2
    ):
        await message.reply("𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐅ɪʟᴛᴇʀ ᴀ 𝐍ᴀᴍᴇ!")  
        return 
    
    filter_name, filter_reason = get_text_reason(message)
    if (
        message.reply_to_message
        and not len(message.command) >=2
    ):
        await message.reply("𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐅ɪʟᴛᴇʀ 𝐒ᴏᴍᴇ 𝐂ᴏɴᴛᴇɴᴛ!")
        return

    content, text, data_type = await GetFIlterMessage(message)
    await add_filter_db(chat_id, filter_name=filter_name, content=content, text=text, data_type=data_type)
    await message.reply(
        f"𝐒ᴀᴠᴇᴅ 𝐅ɪʟᴛᴇʀ '`{filter_name}`'."
    )


@app.on_message(~filters.bot & filters.group, group=4)
async def FilterCheckker(client, message):
    if not message.text:
        return
    text = message.text
    chat_id = message.chat.id
    if (
        len(await get_filters_list(chat_id)) == 0
    ):
        return

    ALL_FILTERS = await get_filters_list(chat_id)
    for filter_ in ALL_FILTERS:
        
        if (
            message.command
            and message.command[0] == 'filter'
            and len(message.command) >= 2
            and message.command[1] ==  filter_
        ):
            return
            
        pattern = r"( |^|[^\w])" + re.escape(filter_) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            filter_name, content, text, data_type = await get_filter(chat_id, filter_)
            await SendFilterMessage(
                message=message,
                filter_name=filter_,
                content=content,
                text=text,
                data_type=data_type
            )

@app.on_message(filters.command('filters') & filters.group)
async def _filters(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title 
    if message.chat.type == 'private':
        chat_title = 'local'
    FILTERS = await get_filters_list(chat_id)
    
    if len(FILTERS) == 0:
        await message.reply(
            f'𝐍ᴏ 𝐅ɪʟᴛᴇʀꜱ ɪɴ {chat_title}.'
        )
        return

    filters_list = f'List of filters in {chat_title}:\n'
    
    for filter_ in FILTERS:
        filters_list += f'- `{filter_}`\n'
    
    await message.reply(
        filters_list
    )


@app.on_message(filters.command('stopall') & admin_filter)
async def stopall(client, message):
    if not message.from_user:
        return
    chat_id = message.chat.id
    chat_title = message.chat.title 
    user = await client.get_chat_member(chat_id, message.from_user.id)
    if not user.status == ChatMemberStatus.OWNER :
        return await message.reply_text("𝐎ɴʟʏ 𝐎ᴡɴᴇʀ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ!!") 

    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐅ɪʟᴛᴇʀꜱ', callback_data='custfilters_stopall')],
        [InlineKeyboardButton(text='𝐂ᴀɴᴄᴇʟ', callback_data='custfilters_cancel')]]
    )

    await message.reply(
        text=(f'𝐀ʀᴇ 𝐘ᴏᴜ 𝐒ᴜʀᴇ 𝐘ᴏᴜ 𝐖ᴀɴᴛ ᴛᴏ 𝐒ᴛᴏᴘ **𝐀𝐋𝐋** 𝐅ɪʟᴛᴇʀꜱ ɪɴ {chat_title}? 𝐓ʜɪꜱ 𝐀ᴄᴛɪᴏɴ ɪꜱ 𝐈ʀʀᴇᴠᴇʀꜱɪʙʟᴇ.'),
        reply_markup=KEYBOARD
    )


@app.on_callback_query(filters.regex("^custfilters_"))
async def stopall_callback(client, callback_query: CallbackQuery):  
    if not callback_query.from_user:
        return
    chat_id = callback_query.message.chat.id 
    query_data = callback_query.data.split('_')[1]  

    user = await client.get_chat_member(chat_id, callback_query.from_user.id)

    if not user.status == ChatMemberStatus.OWNER :
        return await callback_query.answer("𝐎ɴʟʏ 𝐎ᴡɴᴇʀ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ!!", show_alert=True) 
    
    if query_data == 'stopall':
        await stop_all_db(chat_id)
        await callback_query.edit_message_text(text="𝐈'ᴠᴇ 𝐃ᴇʟᴇᴛᴇᴅ 𝐀ʟʟ 𝐂ʜᴀᴛ 𝐅ɪʟᴛᴇʀꜱ.")
    
    elif query_data == 'cancel':
        await callback_query.edit_message_text(text='𝐂ᴀɴᴄᴇʟʟᴇᴅ.')



@app.on_message(filters.command('stopfilter') & admin_filter)
@user_admin
async def stop(client, message):
    chat_id = message.chat.id
    if not (len(message.command) >= 2):
        await message.reply('𝐔ꜱᴇ 𝐇ᴇʟᴘ ᴛᴏ 𝐊ɴᴏᴡ ᴛʜᴇ 𝐂ᴏᴍᴍᴀɴᴅ 𝐔ꜱᴀɢᴇ')
        return
    
    filter_name = message.command[1]
    if (filter_name not in await get_filters_list(chat_id)):
        await message.reply("𝐘ᴏᴜ 𝐇ᴀᴠᴇɴ'ᴛ 𝐒ᴀᴠᴇᴅ 𝐀ɴʏ 𝐅ɪʟᴛᴇʀꜱ ᴏɴ 𝐓ʜɪꜱ 𝐖ᴏʀᴅ 𝐘ᴇᴛ!")
        return
    
    await stop_db(chat_id, filter_name)
    await message.reply(f"𝐈'ᴠᴇ 𝐒ᴛᴏᴘᴘᴇᴅ `{filter_name}`.")
    
