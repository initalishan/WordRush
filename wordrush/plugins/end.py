from wordrush.core.client import wordrush
from telethon import events
from wordrush.config import is_playing, guess_history


@wordrush.on(events.NewMessage(pattern=r"(?i)\/end"))
async def game_end(event):
    chat_id = event.chat_id
    user = await event.get_sender()
    chat = await event.get_chat()
    if not event.is_private:
        rights = await wordrush.get_permissions(chat.id, user.id)
        if not rights.is_admin:
            await event.reply("You must be an admin to use this.")
            return
    if not chat_id in is_playing:
        await event.respond("There is no game in **progress.**")
    else:
        await event.respond(f"Game ended!\nCorrect word was **{is_playing[chat_id]}**\nStart new game with **/new**")
        del is_playing[chat_id]
        del guess_history[chat_id]