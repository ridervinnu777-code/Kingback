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
import asyncio
import os
import shutil
import socket
from datetime import datetime
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from AZURAMUSIC import app
from AZURAMUSIC.misc import HAPP, SUDOERS, XCB
from AZURAMUSIC.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from AZURAMUSIC.utils.decorators.language import language
from AZURAMUSIC.utils.pastebin import AZURABin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(["getlog", "logs", "getlogs"]) & SUDOERS)
@language
async def log_(client, message, _):
    try:
        await message.reply_document(document="log.txt")
    except:
        await message.reply_text(_["server_1"])


@app.on_message(filters.command(["update", "gitpull"]) & SUDOERS)
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["server_2"])
    response = await message.reply_text(_["server_3"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["server_4"])
    except InvalidGitRepositoryError:
        return await response.edit(_["server_5"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]
    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(_["server_6"])
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: <𝐀 𝐇ʀᴇꜰ={REPO_}/commit/{info}>{info.summary}</a> 𝐁ʏ -> {info.author}</b>\n\t\t\t\t<b>➥ 𝐂ᴏᴍᴍɪᴛᴇᴅ ᴏɴ :</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>𝐀 𝐍ᴇᴡ 𝐔ᴘᴅᴀᴛᴇ ɪꜱ 𝐀ᴠᴀɪʟᴀʙʟᴇ ꜰᴏʀ ᴛʜᴇ 𝐁ᴏᴛ !</b>\n\n➣ 𝐏ᴜꜱʜɪɴɢ 𝐔ᴘᴅᴀᴛᴇꜱ 𝐍ᴏᴡ\n\n<b><u>𝐔ᴘᴅᴀᴛᴇꜱ:</u></b>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await AZURABin(updates)
        nrs = await response.edit(
            f"<b>𝐀 𝐍ᴇᴡ 𝐔ᴘᴅᴀᴛᴇ ɪꜱ 𝐀ᴠᴀɪʟᴀʙʟᴇ ꜰᴏʀ ᴛʜᴇ 𝐁ᴏᴛ !</b>\n\n➣ 𝐏ᴜꜱʜɪɴɢ 𝐔ᴘᴅᴀᴛᴇꜱ 𝐍ᴏᴡ\n\n<u><b>𝐔ᴘᴅᴀᴛᴇꜱ :</b></u>\n\n<𝐀 𝐇ʀᴇꜰ={url}>𝐂ʜᴇᴄᴋ 𝐔ᴘᴅᴀᴛᴇꜱ</a>"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    os.system("git stash &> /dev/null && git pull")

    try:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    chat_id=int(x),
                    text=_["server_8"].format(app.mention),
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except:
                pass
        await response.edit(f"{nrs.text}\n\n{_['server_7']}")
    except:
        pass

    if await is_heroku():
        try:
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(f"{nrs.text}\n\n{_['server_9']}")
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=_["server_10"].format(err),
            )
    else:
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && bash start")
        exit()


@app.on_message(filters.command(["restart"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("𝐑ᴇꜱᴛᴀʀᴛɪɴɢ...")
    ac_chats = await get_active_chats()
    for x in ac_chats:
        try:
            await app.send_message(
                chat_id=int(x),
                text=f"{app.mention} 𝐈ꜱ 𝐑ᴇꜱᴛᴀʀᴛɪɴɢ...\n\n𝐘ᴏᴜ 𝐂ᴀɴ 𝐒ᴛᴀʀᴛ 𝐏ʟᴀʏɪɴɢ 𝐀ɢᴀɪɴ 𝐀ꜰᴛᴇʀ 15-20 𝐒ᴇᴄᴏɴᴅꜱ.",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except:
            pass

    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "» 𝐑ᴇꜱᴛᴀʀᴛ 𝐏ʀᴏᴄᴇꜱꜱ 𝐒ᴛᴀʀᴛᴇᴅ, 𝐏ʟᴇᴀꜱᴇ 𝐖ᴀɪᴛ ꜰᴏʀ 𝐅ᴇᴡ 𝐒ᴇᴄᴏɴᴅꜱ 𝐔ɴᴛɪʟ ᴛʜᴇ 𝐁ᴏᴛ 𝐒ᴛᴀʀᴛꜱ..."
    )
    os.system(f"kill -9 {os.getpid()} && bash start")
