from telethon import events
from wordrush.core.client import wordrush
from wordrush.config import start_caption
from wordrush.misc.safedict import SafeDict
from wordrush.utils.buttons import start_buttons, start_group_buttons

@wordrush.on(events.NewMessage(pattern="(?i)\/start"))
async def start_handler(event):
    user = await event.get_sender()
    mention = f"[{user.first_name}](tg://user?id={user.id})"
    safe_data = SafeDict(
        mention=mention
        )
    formated_start_caption = start_caption.format_map(safe_data)
    if event.is_private:
        await event.respond(
        formated_start_caption, buttons=start_buttons
        )
    else:
        await event.respond(formated_start_caption, buttons=start_group_buttons)