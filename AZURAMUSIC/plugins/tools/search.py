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
from traceback import format_exc
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackSearch
from search_engine_parser.core.exceptions import NoResultsFound, NoResultsOrTrafficError
from AZURAMUSIC import app
from pyrogram import filters


gsearch = GoogleSearch()
stsearch = StackSearch()


def ikb(rows=None, back=False, todo="start_back"):
    """
    rows = pass the rows
    back - if want to make back button
    todo - callback data of back button
    """
    if rows is None:
        rows = []
    lines = []
    try:
        for row in rows:
            line = []
            for button in row:
                btn_text = button.split(".")[1].capitalize()
                button = btn(btn_text, button)  
                line.append(button)
            lines.append(line)
    except AttributeError:
        for row in rows:
            line = []
            for button in row:
                button = btn(*button)  
                line.append(button)
            lines.append(line)
    except TypeError:
        # make a code to handel that error
        line = []
        for button in rows:
            button = btn(*button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    if back: 
        back_btn = [(btn("𝐁ᴀᴄᴋ", todo))]
        lines.append(back_btn)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})






@app.on_message(filters.command('google'))
async def search_(app: app, msg: Message):
    split = msg.text.split(None, 1)
    if len(split) == 1:
        return await msg.reply_text("**𝐆ɪᴠᴇ 𝐐ᴜᴇʀʏ ᴛᴏ 𝐒ᴇᴀʀᴄʜ**")
    to_del = await msg.reply_text("**𝐒ᴇᴀʀᴄʜɪɴɢ ᴏɴ 𝐆ᴏᴏɢʟᴇ...**")
    query = split[1]
    try:
        result = await gsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"**𝐇ᴇʀᴇ ᴀʀᴇ ᴛʜᴇ 𝐑ᴇꜱᴜʟᴛꜱ ᴏꜰ 𝐑ǫᴜᴇꜱᴛᴇᴅ : {query.title()}**"
        await to_del.delete()
        await msg.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await msg.reply_text("**𝐍ᴏ 𝐑ᴇꜱᴜʟᴛ 𝐅ᴏᴜɴᴅ 𝐂ᴏʀʀᴇꜱᴘᴏɴᴅɪɴɢ ᴛᴏ 𝐘ᴏᴜʀ 𝐐ᴜᴇʀʏ**")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await msg.reply_text("****𝐍ᴏ 𝐑ᴇꜱᴜʟᴛ 𝐅ᴏᴜɴᴅ 𝐃ᴜᴇ ᴛᴏ 𝐓ᴏᴏ 𝐌ᴀɴʏ 𝐓ʀᴀꜰꜰɪᴄ**")
        return
    except Exception as e:
        await to_del.delete()
        await msg.reply_text(f"**𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ᴇɴᴛ 𝐖ʀᴏɴɢ :\n𝐑ᴇᴘᴏʀᴛ ᴀᴛ ɪᴛ** @vinnu_exe")
        print(f"error : {e}")
        return



@app.on_message(filters.command('stack'))
async def stack_search_(app: app, msg: Message):
    split = msg.text.split(None, 1)
    if len(split) == 1:
        return await msg.reply_text("**𝐆ɪᴠᴇ 𝐐ᴜᴇʀʏ ᴛᴏ 𝐒ᴇᴀʀᴄʜ**")
    to_del = await msg.reply_text("**𝐒ᴇᴀʀᴄʜɪɴɢ ᴏɴ 𝐆ᴏᴏɢʟᴇ...**")
    query = split[1]
    try:
        result = await stsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"**𝐇ᴇʀᴇ ᴀʀᴇ ᴛʜᴇ 𝐑ᴇꜱᴜʟᴛꜱ ᴏꜰ 𝐑ǫᴜᴇꜱᴛᴇᴅ : {query.title()}**"
        await to_del.delete()
        await msg.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await msg.reply_text("**𝐍ᴏ 𝐑ᴇꜱᴜʟᴛ 𝐅ᴏᴜɴᴅ 𝐂ᴏʀʀᴇꜱᴘᴏɴᴅɪɴɢ ᴛᴏ 𝐘ᴏᴜʀ 𝐐ᴜᴇʀʏ**")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await msg.reply_text("****𝐍ᴏ 𝐑ᴇꜱᴜʟᴛ 𝐅ᴏᴜɴᴅ 𝐃ᴜᴇ ᴛᴏ 𝐓ᴏᴏ 𝐌ᴀɴʏ 𝐓ʀᴀꜰꜰɪᴄ**")
        return
    except Exception as e:
        await to_del.delete()
        await msg.reply_text(f"**𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ᴇɴᴛ 𝐖ʀᴏɴɢ :\n𝐑ᴇᴘᴏʀᴛ ᴀᴛ ɪᴛ** @vinnu_exe")
        print(f"error : {e}")
        return




