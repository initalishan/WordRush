from wordrush.core.database import users_col, groups_col
from wordrush.config import user_log_caption, group_log_caption
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from wordrush.core.client import wordrush
from wordrush.misc.safedict import SafeDict
from dotenv import load_dotenv
from os import environ, remove
from telethon import Button, events

load_dotenv()
chat_log = int(environ["chat_log"])

async def add_user_db(event):
    user = await event.get_sender()
    user_id = user.id
    if not users_col.find_one({"user_id": user_id}):
        username = user.username or "Anonymous"
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        full_name = (first_name + " " + last_name).strip()
        safe_data = SafeDict(
            username=username,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            sender_id=user_id,
        )
        users_col.insert_one({"user_id": user_id})
        formated_user_log_caption = user_log_caption.format_map(safe_data)
        await wordrush.send_message(
            chat_log,
            formated_user_log_caption,
            force_document=False
                )
        
async def add_group_db(event):
    chat = await event.get_chat()
    chat_id = int(f"-100{chat.id}" if not str(chat.id).startswith("-100") else chat.id)
    if not groups_col.find_one({"group_id": chat_id}):
        groups_col.insert_one({"group_id": chat_id})
        full_chat = await zhunehra(GetFullChannelRequest(channel=chat_id))
        channel_obj = full_chat.chats[0]
        full_info = full_chat.full_chat 
        full_name = channel_obj.title
        username = channel_obj.username if channel_obj.username else None
        safe_data = SafeDict(
            full_name=full_name,
            username=username,
            chat_id=chat_id
        )
        formated_group_log_caption = group_log_caption.format_map(safe_data)
        try:
            result = await wordrush(ExportChatInviteRequest(chat_id))
            invite_link = result.link
            invite_button = [
                [Button.url("See Group", invite_link)]
            ]
        except Exception:
            invite_button = [
                [Button.inline("See Group", data=b"invite_failed")]
            ]
        await wordrush.send_message(
            chat_log,
            formated_group_log_caption,
            buttons=invite_button,
            force_document=False
            )
        
@wordrush.on(events.CallbackQuery(data=b"invite_failed"))
async def invite_failed_callback(event):
    await event.answer("Failed to create invite link because zhunehra is not admin and group is private.")

@wordrush.on(events.NewMessage)
async def logs(event):
    if event.is_private:
        user = await event.get_sender()
        user_id = user.id
        username = user.username or "Anonymous"
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        full_name = (first_name + " " + last_name).strip()
        await add_user_db(event)
        try:
            message = event.message.message
        except:
            message = "User send a file."
        if username != "Anonymous":
            mention = f"[{full_name}](https://t.me/{username})"
        else:
            mention = f"[{full_name}](tg://user?id={user_id})"
        await wordrush.send_message(chat_log, f"Catch New Message!\nSender: {mention}\nSender_id: {user_id}\nMessage: {message}")
    else:
        await add_group_db(event)
        