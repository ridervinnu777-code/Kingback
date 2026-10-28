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
import git
import shutil
import os
from AZURAMUSIC import app


@app.on_message(filters.command(["downloadrepo"]))
def download_repo(_, message):
    if len(message.command) != 2:
        message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐏ʀᴏᴠɪᴅᴇ ᴛʜᴇ 𝐆ɪᴛʜᴜʙ 𝐑ᴇᴘᴏꜱɪᴛᴏʀʏ 𝐔𝐑𝐋 𝐀ꜰᴛᴇʀ ᴛʜᴇ 𝐂ᴏᴍᴍᴀɴᴅ. 𝐄xᴀᴍᴘʟᴇ: /downloadrepo 𝐑ᴇᴘᴏ 𝐔𝐑𝐋 ")
        return

    repo_url = message.command[1]
    zip_path = download_and_zip_repo(repo_url)

    if zip_path:
        with open(zip_path, "rb") as zip_file:
            message.reply_document(zip_file)
        os.remove(zip_path)
    else:
        message.reply_text("𝐔ɴᴀʙʟᴇ ᴛᴏ 𝐃ᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ 𝐒ᴘᴇᴄɪꜰɪᴇᴅ 𝐆ɪᴛʜᴜʙ 𝐑ᴇᴘᴏꜱɪᴛᴏʀʏ.")


def download_and_zip_repo(repo_url):
    try:
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        repo_path = f"{repo_name}"
        
        # Clone the repository
        repo = git.Repo.clone_from(repo_url, repo_path)
        
        # Create a zip file of the repository
        shutil.make_archive(repo_path, 'zip', repo_path)

        return f"{repo_path}.zip"
    except Exception as e:
        print(f"Error downloading and zipping GitHub repository: {e}")
        return None
    finally:
        if os.path.exists(repo_path):
            shutil.rmtree(repo_path)
