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
from AZURAMUSIC.utils.Azura_ban import admin_filter
import os
import csv
from pyrogram import Client, filters
from AZURAMUSIC import app

@app.on_message(filters.command("user") & admin_filter)
def user_command(client, message):
    
    chat_members = app.get_chat_members(message.chat.id)

    
    members_list = []
    for member in chat_members:
        members_list.append({
            "username": member.user.username,
            "userid": member.user.id
        })

    
    with open("members.txt", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "userid"])
        writer.writeheader()
        for member in members_list:
            writer.writerow(member)

    # Send the text file as a reply to the message
    app.send_document(message.chat.id, "members.txt")


# Command handler for /givelink command
@app.on_message(filters.command("givelink"))
async def give_link_command(client, message):
    # Generate an invite link for the chat where the command is used
    chat = message.chat.id
    link = await app.export_chat_invite_link(chat)
    await message.reply_text(f"𝐇ᴇʀᴇ'ꜱ ᴛʜᴇ 𝐈ɴᴠɪᴛᴇ 𝐋ɪɴᴋ ꜰᴏʀ 𝐓ʜɪꜱ 𝐂ʜᴀᴛ:\n{link}")
