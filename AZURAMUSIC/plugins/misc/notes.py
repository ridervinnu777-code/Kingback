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
from config import BOT_USERNAME
from pyrogram import filters
from AZURAMUSIC.utils.Azura_ban import admin_filter
from AZURAMUSIC.mongo.notesdb import *
from AZURAMUSIC.utils.notes_func import GetNoteMessage, exceNoteMessageSender, privateNote_and_admin_checker
from AZURAMUSIC.utils.shivdb import user_admin
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , Message , CallbackQuery
from pyrogram.enums import ChatMemberStatus


@app.on_message(filters.command("save") & admin_filter)
@user_admin
async def _save(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    if message.reply_to_message and not len(message.command) >= 2:
        return await message.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐍ᴏᴛᴇ ᴀ 𝐍ᴀᴍᴇ!")
    
    if not message.reply_to_message and not len(message.command) >= 3:
        return await message.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐍ᴏᴛᴇ 𝐒ᴏᴍᴇ 𝐂ᴏɴᴛᴇɴᴛ!")
    
    NoteName = message.command[1]
    Content, Text, DataType = GetNoteMessage(message)
    await SaveNote(chat_id, NoteName, Content, Text, DataType)

    await message.reply_text(f"𝐈'ᴠᴇ 𝐒ᴀᴠᴇᴅ 𝐍ᴏᴛᴇ `{NoteName}` 𝐈ɴ {chat_title}.")
    



@app.on_message(filters.command("get") & admin_filter)
async def _getnote(client, message):
    chat_id = message.chat.id
    if not len(message.command) >= 2:
        return await message.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐍ᴏᴛᴇ ᴀ 𝐍ᴀᴍᴇ!")  
    note_name = message.command[1]
    if not await isNoteExist(chat_id, note_name):
         return await message.reply_text("𝐍ᴏᴛᴇ 𝐍ᴏᴛ 𝐅ᴏᴜɴᴅ")
    await send_note(message, note_name)
    

@app.on_message(filters.regex(pattern=(r"^#[^\s]+")) & filters.group)
async def regex_get_note(client, message):
    chat_id = message.chat.id
    if message.from_user:
        note_name = message.text.split()[0].replace('#', '')
        if await isNoteExist(chat_id, note_name):
            await send_note(message, note_name)


PRIVATE_NOTES_TRUE = ['on', 'true', 'yes', 'y']
PRIVATE_NOTES_FALSE = ['off', 'false', 'no', 'n']

@app.on_message(filters.command("privatenotes") & filters.group)
@user_admin
async def PrivateNote(client, message):
    chat_id = message.chat.id
    if len(message.command) >= 2:
        if (
            message.command[1] in PRIVATE_NOTES_TRUE
        ):
            await set_private_note(chat_id, True)
            await message.reply(
                "𝐍ᴏᴡ 𝐈 𝐖ɪʟʟ 𝐒ᴇɴᴅ ᴀ 𝐌ᴇꜱꜱᴀɢᴇ ᴛᴏ 𝐘ᴏᴜʀ 𝐂ʜᴀᴛ ᴡɪᴛʜ ᴀ 𝐁ᴜᴛᴛᴏɴ 𝐑ᴇᴅɪʀᴇᴄᴛɪɴɢ ᴛᴏ 𝐏𝐌, 𝐖ʜᴇʀᴇ ᴛʜᴇ 𝐔ꜱᴇʀ 𝐖ɪʟʟ 𝐑ᴇᴄᴇɪᴠᴇ ᴛʜᴇ 𝐍ᴏᴛᴇ.",
                quote=True
            )

        elif (
            message.command[1] in PRIVATE_NOTES_FALSE
        ):
            await set_private_note(chat_id, False)
            await message.reply(
                "𝐈 𝐖ɪʟʟ 𝐍ᴏᴡ 𝐒ᴇɴᴅ 𝐍ᴏᴛᴇꜱ 𝐒ᴛʀᴀɪɢʜᴛ ᴛᴏ ᴛʜᴇ 𝐆ʀᴏᴜᴘ.",
                quote=True
            )  
        else:
            await message.reply(
                f"𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐆ᴇᴛ 𝐁ᴏᴏʟᴇᴀɴ 𝐕ᴀʟᴜᴇ ꜰʀᴏᴍ 𝐈ɴᴘᴜᴛ:\n\n 𝐄xᴘᴇᴄᴛᴇᴅ 𝐎ɴᴇ ᴏꜰ 𝐘/𝐘ᴇꜱ/ᴏɴ/𝐓ʀᴜᴇ ᴏʀ 𝐍/𝐍ᴏ/𝐎ꜰꜰ/𝐅ᴀʟꜱᴇ; 𝐆ᴏᴛ: {message.command[1]}",
                quote=True
            )
    else:
        if await is_pnote_on(chat_id):
            await message.reply(
                "𝐘ᴏᴜʀ 𝐍ᴏᴛᴇꜱ ᴀʀᴇ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐁ᴇɪɴɢ 𝐒ᴇɴᴛ ɪɴ 𝐏ʀɪᴠᴀᴛᴇ. 𝐒𝐇𝐔𝐊𝐋𝐀𝐌𝐔𝐒𝐈𝐂 𝐖ɪʟʟ 𝐒ᴇɴᴅ ᴀ 𝐒ᴍᴀʟʟ 𝐍ᴏᴛᴇ ᴡɪᴛʜ ᴀ 𝐁ᴜᴛᴛᴏɴ 𝐖ʜɪᴄʜ 𝐑ᴇᴅɪʀᴇᴄᴛꜱ ᴛᴏ ᴀ 𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ.",
                quote=True
            )
        else:
            await message.reply(
                "𝐘ᴏᴜʀ 𝐍ᴏᴛᴇꜱ ᴀʀᴇ 𝐂ᴜʀʀᴇɴᴛʟʏ 𝐁ᴇɪɴɢ 𝐒ᴇɴᴛ ɪɴ ᴛʜᴇ 𝐆ʀᴏᴜᴘ.",
                quote=True
            )
            
@app.on_message(filters.command("clear") & admin_filter)
@user_admin
async def Clear_Note(client, message):
    chat_id = message.chat.id 
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "𝐘ᴏᴜ 𝐍ᴇᴇᴅ ᴛᴏ 𝐆ɪᴠᴇ ᴛʜᴇ 𝐍ᴏᴛᴇ ᴀ 𝐍ᴀᴍᴇ!",
            quote=True
        )
        return
    
    note_name = message.command[1].lower()

    if await isNoteExist(chat_id, note_name):
        await ClearNote(chat_id, note_name)

        await message.reply(
            f"𝐈'ᴠᴇ 𝐑ᴇᴍᴏᴠᴇᴅ ᴛʜᴇ 𝐍ᴏᴛᴇ `{note_name}`!.",
            quote=True
        )
    else:
        await message.reply(
            "𝐘ᴏᴜ 𝐇ᴀᴠᴇɴ'ᴛ 𝐒ᴀᴠᴇᴅ ᴀ 𝐍ᴏᴛᴇ ᴡɪᴛʜ 𝐓ʜɪꜱ 𝐍ᴀᴍᴇ 𝐘ᴇᴛ!",
            quote=True
        )


@app.on_message(filters.command("clearall") & admin_filter)
async def ClearAll_Note(client, message):
    owner_id = message.from_user.id
    chat_id = message.chat.id 
    chat_title = message.chat.title
    user = await client.get_chat_member(chat_id,owner_id)
    if not user.status == ChatMemberStatus.OWNER :
        return await message.reply_text("𝐎ɴʟʏ 𝐎ᴡɴᴇʀ 𝐂ᴀɴ 𝐔ꜱᴇ 𝐓ʜɪꜱ!!") 

    note_list = await NoteList(chat_id)
    if note_list == 0:
        await message.reply(
            f"𝐍ᴏ 𝐍ᴏᴛᴇꜱ ɪɴ {chat_title}",
            quote=True
        )
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text='𝐃ᴇʟᴇᴛᴇ 𝐀ʟʟ 𝐍ᴏᴛᴇꜱ', callback_data=f'clearallnotes_clear_{owner_id}_{chat_id}')
        ],
        [
            InlineKeyboardButton(text='𝐂ᴀɴᴄᴇʟ', callback_data=f'clearallnotes_cancel_{owner_id}')
        ]]
    )
    await message.reply(
        f"𝐀ʀᴇ 𝐘ᴏᴜ 𝐒ᴜʀᴇ 𝐘ᴏᴜ 𝐖ᴀɴᴛ ᴛᴏ 𝐂ʟᴇᴀʀ **𝐀𝐋𝐋** 𝐍ᴏᴛᴇꜱ ɪɴ {chat_title}? 𝐓ʜɪꜱ 𝐀ᴄᴛɪᴏɴ ɪꜱ 𝐈ʀʀᴇᴠᴇʀꜱɪʙʟᴇ.",
        reply_markup=keyboard,
        quote=True
    )

@app.on_callback_query(filters.regex("^clearallnotes_"))
async def ClearAllCallback(client, callback_query: CallbackQuery):
    query_data = callback_query.data.split('_')[1]
    owner_id = int(callback_query.data.split('_')[2])
    user_id = callback_query.from_user.id 

    if owner_id == user_id:
        if query_data == 'clear':
            chat_id = int(callback_query.data.split('_')[3])
            await ClearAllNotes(chat_id)
            await callback_query.edit_message_text("Deleted all chat notes.") 
            return
            
        elif query_data == 'cancel':
            await callback_query.edit_message_text("Cancelled.")
    else:
        await callback_query.answer("𝐎ɴʟʏ 𝐀ᴅᴍɪɴꜱ 𝐂ᴀɴ 𝐄xᴇᴄᴜᴛᴇ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ!")
                         
@app.on_message(filters.command(['notes', 'saved']) & filters.group)
async def Notes(client, message):
    
    chat_id = message.chat.id
    chat_title = message.chat.title

    Notes_list = await NoteList(chat_id)
    
    NoteHeader = f"List of notes  in {chat_title}:\n"
    if (
        len(Notes_list) != 0
    ): 
        for notes in Notes_list:
            NoteName = f" • `#{notes}`\n"
            NoteHeader += NoteName
        await message.reply(
            (
                f"{NoteHeader}\n"
                "𝐘ᴏᴜ 𝐂ᴀɴ 𝐑ᴇᴛʀɪᴇᴠᴇ 𝐓ʜᴇꜱᴇ 𝐍ᴏᴛᴇꜱ ʙʏ 𝐔ꜱɪɴɢ `/get notename`, ᴏʀ `#notename`"
            ),
            quote=True
        )
        
    else:
        await message.reply(
            f"𝐍ᴏ 𝐍ᴏᴛᴇꜱ ɪɴ {chat_title}.",
            quote=True
        )        

async def send_note(message: Message, note_name: str):
    chat_id = message.chat.id  
    content, text, data_type = await GetNote(chat_id, note_name)
    privateNote, allow = await privateNote_and_admin_checker(message, text)   
    if allow:
        if privateNote == None:
            if await is_pnote_on(chat_id):
                await PrivateNoteButton(message, chat_id, note_name)
            else:
                await exceNoteMessageSender(message, note_name)
            
        elif privateNote is not None:
            if await is_pnote_on(chat_id):
                if privateNote:
                    await PrivateNoteButton(message, chat_id, note_name)
                else:
                    await exceNoteMessageSender(message, note_name)
            else: 
                if privateNote:
                    await PrivateNoteButton(message, chat_id, note_name)
                else:
                    await exceNoteMessageSender(message, note_name)
                    
                    

async def note_redirect(message):
    chat_id = int(message.command[1].split('_')[1])
    note_name = message.command[1].split('_')[2]
    await exceNoteMessageSender(message, note_name, from_chat_id=chat_id)

async def PrivateNoteButton(message, chat_id, NoteName):
    PrivateNoteButton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text='𝐂ʟɪᴄᴋ 𝐌ᴇ!', url=f'http://t.me/{BOT_USERNAME}?start=note_{chat_id}_{NoteName}')
            ]
        ]
    )
    await message.reply(
        text=f"𝐓ᴀᴘ 𝐇ᴇʀᴇ ᴛᴏ 𝐕ɪᴇᴡ '{NoteName}' 𝐈ɴ 𝐘ᴏᴜʀ 𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ.",
        reply_markup=PrivateNoteButton
    )


#
"""**                                                                         
────────────────────────────────────────────────────────────────────────
─████████████────██████████████──████████──████████──████████──████████─
─██░░░░░░░░████──██░░░░░░░░░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─██░░████░░░░██──██░░██████░░██──████░░██──██░░████──████░░██──██░░████─
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░░░░░░░░░██──────██░░░░░░██──────────██░░░░░░██─────
─██░░██──██░░██──██░░██████░░██────████░░░░░░████──────████░░░░░░████───
─██░░██──██░░██──██░░██──██░░██────██░░░░██░░░░██──────██░░░░██░░░░██───
─██░░████░░░░██──██░░██──██░░██──████░░██──██░░████──████░░██──██░░████─
─██░░░░░░░░████──██░░██──██░░██──██░░░░██──██░░░░██──██░░░░██──██░░░░██─
─████████████────██████──██████──████████──████████──████████──████████─
────────────────────────────────────────────────────────────────────────**"""
