from wordrush.core.client import wordrush
from telethon import events
from wordrush.config import is_playing


@wordrush.on(events.NewMessage(pattern=r"(i?)\/end"))
async def game_end(event):
    chat_id = event.chat_id
    if not is_playing[chat_id]:
        await event.respond("There is no game in **progress.**")
    else:
        await event.respond(f"Game ended!\nCorrect word was **{is_playing[chat_id]}**\nStart new game with **/new**")
        del is_playing[chat_id]