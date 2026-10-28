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
from pyrogram import Client, filters
import os
import zipfile
from AZURAMUSIC import app


def zip_file(file_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        zip_file.write(file_path, os.path.basename(file_path))


def unzip_file(zip_file_path, output_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        zip_file.extractall(output_folder)


@app.on_message(filters.command("zip"))
def zip_command(client, message):
    if message.reply_to_message and message.reply_to_message.document:
        original_file = client.download_media(message.reply_to_message)
        zip_file_path = f"{original_file}.zip"
        zip_file(original_file, zip_file_path)

        message.reply_document(zip_file_path)

       
        os.remove(zip_file_path)
    else:
        message.reply_text("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐅ɪʟᴇ ᴡɪᴛʜ /zip ᴛᴏ 𝐂ᴏɴᴠᴇʀᴛ ɪᴛ ᴛᴏ ᴀ 𝐙ɪᴘ 𝐅ɪʟᴇ.")


@app.on_message(filters.command("unzip"))
def unzip_command(client, message):
    if message.reply_to_message and message.reply_to_message.document and message.reply_to_message.document.file_name.endswith(".zip"):
        zip_file_path = client.download_media(message.reply_to_message)
        output_folder = f"{zip_file_path}_unzipped"

      
        os.makedirs(output_folder, exist_ok=True)

        unzip_file(zip_file_path, output_folder)

        
        for root, dirs, files in os.walk(output_folder):
            for file in files:
                file_path = os.path.join(root, file)
                message.reply_document(file_path)

        
        os.rmdir(output_folder)
    else:
        message.reply_text("𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐙ɪᴘ 𝐅ɪʟᴇ ᴡɪᴛʜ /unzip ᴛᴏ 𝐄xᴛʀᴀᴄᴛ 𝐈ᴛꜱ 𝐂ᴏɴᴛᴇɴᴛꜱ.")
        
