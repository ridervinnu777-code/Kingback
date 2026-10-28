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
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPrivileges
from pyrogram.errors import ChatAdminRequired
from functools import wraps
from AZURAMUSIC import app

# ── KripanshEmojis_by_fStikBot pack IDs ──
_KE_CROWN  = 6129705083501293112   # 👑
_KE_STAR   = 6129915811776698328   # 🌟
_KE_FIRE   = 6129792056589031358   # 🔥
_KE_WARN   = 6129782440157256336   # ⚠️
_KE_OK     = 6129812419028982717   # ✅
_KE_BLOCK  = 6129840374971112593   # 🚫
_KE_SKULL  = 6132184924603554220   # 💀
_KE_ANGRY  = 6129530544620314433   # 🤬
_KE_ELITE  = 6129509499280563691   # 💎
_KE_ANGEL  = 6129518870899203008   # 👼

def ke(eid, fb):
    return f'<emoji id={eid}>{fb}</emoji>'

def mention(user_id, name):
    return f"[{name}](tg://user?id={user_id})"

def admin_required(*privileges):
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message):
            if not message.from_user:
                await message.reply_text("𝐘ᴏᴜ ᴀʀᴇ ᴀɴ 𝐀ɴᴏɴʏᴍᴏᴜꜱ 𝐀ᴅᴍɪɴ. 𝐏ʟᴇᴀꜱᴇ 𝐔ɴʜɪᴅᴇ 𝐘ᴏᴜʀ 𝐀ᴄᴄᴏᴜɴᴛ ᴛᴏ 𝐔ꜱᴇ 𝐓ʜɪꜱ 𝐂ᴏᴍᴍᴀɴᴅ.")
                return

            member = await message.chat.get_member(message.from_user.id)
            if member.status == enums.ChatMemberStatus.OWNER:
                return await func(client, message)
            elif member.status == enums.ChatMemberStatus.ADMINISTRATOR:
                if not member.privileges:
                    await message.reply_text("𝐂ᴀɴɴᴏᴛ 𝐑ᴇᴛʀɪᴇᴠᴇ 𝐘ᴏᴜʀ 𝐀ᴅᴍɪɴ 𝐏ʀɪᴠɪʟᴇɢᴇꜱ.")
                    return
                missing_privileges = [priv for priv in privileges if not getattr(member.privileges, priv, False)]
                if missing_privileges:
                    await message.reply_text(f"𝐘ᴏᴜ 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ ᴛʜᴇ 𝐑ᴇǫᴜɪʀᴇᴅ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴꜱ: {', '.join(missing_privileges)}")
                    return
                return await func(client, message)
            else:
                await message.reply_text("𝐘ᴏᴜ ᴀʀᴇ 𝐍ᴏᴛ ᴀɴ 𝐀ᴅᴍɪɴ.")
                return
        return wrapper
    return decorator

async def extract_user_and_title(message, client):
    user = None
    title = None

    cmd = message.text.strip().split()[0]
    text = message.text[len(cmd):].strip()

    if message.reply_to_message:
        user = message.reply_to_message.from_user
        if not user:
            await message.reply_text("𝐈 𝐂ᴀɴ'ᴛ 𝐅ɪɴᴅ ᴛʜᴇ 𝐔ꜱᴇʀ ɪɴ ᴛʜᴇ 𝐑ᴇᴘʟɪᴇᴅ 𝐌ᴇꜱꜱᴀɢᴇ.")
            return None, None, None
        title = text if text else None
    else:
        args = text.strip().split(maxsplit=1)
        if not args:
            await message.reply_text("𝐏ʟᴇᴀꜱᴇ 𝐒ᴘᴇᴄɪꜰʏ ᴀ 𝐔ꜱᴇʀ ᴏʀ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐔ꜱᴇʀ'ꜱ 𝐌ᴇꜱꜱᴀɢᴇ.")
            return None, None, None
        user_arg = args[0]
        try:
            user = await client.get_users(user_arg)
            if not user:
                await message.reply_text("𝐈 𝐂ᴀɴ'ᴛ 𝐅ɪɴᴅ 𝐓ʜᴀᴛ 𝐔ꜱᴇʀ.")
                return None, None, None
        except Exception:
            await message.reply_text("𝐈 𝐂ᴀɴ'ᴛ 𝐅ɪɴᴅ 𝐓ʜᴀᴛ 𝐔ꜱᴇʀ.")
            return None, None, None
        title = args[1] if len(args) > 1 else None

    return user.id, user.first_name, title

def format_promotion_message(chat_name, user_mention, admin_mention, action):
    if action == "promote":
        hdr = f"{ke(_KE_CROWN,'👑')} {ke(_KE_STAR,'🌟')} <b>𝐔ꜱᴇʀ 𝐏ʀᴏᴍᴏᴛᴇᴅ</b>"
    else:
        hdr = f"{ke(_KE_SKULL,'💀')} {ke(_KE_BLOCK,'🚫')} <b>𝐔ꜱᴇʀ 𝐃ᴇᴍᴏᴛᴇᴅ</b>"
    return (
        f"{hdr}\n\n"
        f"{ke(_KE_ELITE,'💎')} <b>𝐂ʜᴀᴛ :</b> {chat_name}\n"
        f"{ke(_KE_FIRE,'🔥')} <b>𝐔ꜱᴇʀ :</b> {user_mention}\n"
        f"{ke(_KE_CROWN,'👑')} <b>𝐀ᴅᴍɪɴ :</b> {admin_mention}"
    )

@app.on_message(filters.command("promote"))
@admin_required("can_promote_members")
async def promote_command_handler(client, message):
    user_id, first_name, title = await extract_user_and_title(message, client)
    if not user_id:
        return
    try:
        member = await client.get_chat_member(message.chat.id, user_id)
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("𝐓ʜɪꜱ 𝐔ꜱᴇʀ ɪꜱ 𝐀ʟʀᴇᴀᴅʏ ᴀɴ 𝐀ᴅᴍɪɴ.")
            return

        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_delete_messages=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_restrict_members=False,
                can_promote_members=False,
                can_manage_chat=True,
                can_manage_video_chats=True,
                is_anonymous=False,
            )
        )

        if title:
            try:
                await client.set_administrator_title(message.chat.id, user_id, title)
            except Exception as e:
                await message.reply_text(f"𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐒ᴇᴛ 𝐓ɪᴛʟᴇ: {e}")

        user_mention = mention(user_id, first_name)
        admin_mention = mention(message.from_user.id, message.from_user.first_name)
        chat_name = message.chat.title
        msg = format_promotion_message(chat_name, user_mention, admin_mention, action="promote")
        await message.reply_text(msg)
    except ChatAdminRequired:
        await message.reply_text("𝐈 𝐍ᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ 𝐀ᴅᴍɪɴ ᴡɪᴛʜ 𝐏ʀᴏᴍᴏᴛᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {e}")

@app.on_message(filters.command("fullpromote"))
@admin_required("can_promote_members")
async def fullpromote_command_handler(client, message):
    user_id, first_name, title = await extract_user_and_title(message, client)
    if not user_id:
        return
    try:
        member = await client.get_chat_member(message.chat.id, user_id)
        if member.status == enums.ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("𝐓ʜɪꜱ 𝐔ꜱᴇʀ ɪꜱ 𝐀ʟʀᴇᴀᴅʏ ᴀɴ 𝐀ᴅᴍɪɴ.")
            return

        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_change_info=True,
                can_delete_messages=True,
                can_invite_users=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                is_anonymous=False,
                can_manage_video_chats=True,
            )
        )

        if title:
            try:
                await client.set_administrator_title(message.chat.id, user_id, title)
            except Exception as e:
                await message.reply_text(f"𝐅ᴀɪʟᴇᴅ ᴛᴏ 𝐒ᴇᴛ 𝐓ɪᴛʟᴇ: {e}")

        user_mention = mention(user_id, first_name)
        admin_mention = mention(message.from_user.id, message.from_user.first_name)
        chat_name = message.chat.title
        msg = format_promotion_message(chat_name, user_mention, admin_mention, action="promote")
        await message.reply_text(msg)
    except ChatAdminRequired:
        await message.reply_text("𝐈 𝐍ᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ 𝐀ᴅᴍɪɴ ᴡɪᴛʜ 𝐏ʀᴏᴍᴏᴛᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴꜱ.")
    except Exception as e:
        await message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {e}")

@app.on_message(filters.command("demote"))
@admin_required("can_promote_members")
async def demote_command_handler(client, message):
    user_id, first_name, _ = await extract_user_and_title(message, client)
    if not user_id:
        return
    try:
        member = await client.get_chat_member(message.chat.id, user_id)
        if member.status != enums.ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("𝐓ʜɪꜱ 𝐔ꜱᴇʀ ɪꜱ 𝐍ᴏᴛ ᴀɴ 𝐀ᴅᴍɪɴ.")
            return

        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
                is_anonymous=False
            )
        )

        user_mention = mention(user_id, first_name)
        admin_mention = mention(message.from_user.id, message.from_user.first_name)
        chat_name = message.chat.title
        msg = format_promotion_message(chat_name, user_mention, admin_mention, action="demote")
        await message.reply_text(msg)
    except ChatAdminRequired:
        await message.reply_text("𝐈 𝐍ᴇᴇᴅ ᴛᴏ ʙᴇ ᴀɴ 𝐀ᴅᴍɪɴ ᴡɪᴛʜ 𝐏ʀᴏᴍᴏᴛᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴꜱ.")
    except Exception as e:
        if "CHAT_ADMIN_REQUIRED" in str(e):
            await message.reply_text("𝐈 𝐃ᴏɴ'ᴛ 𝐇ᴀᴠᴇ 𝐏ᴇʀᴍɪꜱꜱɪᴏɴ ᴛᴏ 𝐃ᴇᴍᴏᴛᴇ 𝐓ʜɪꜱ 𝐔ꜱᴇʀ.")
        else:
            await message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {e}")
