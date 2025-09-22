from telethon import events
from wordrush.core.client import wordrush

@wordrush.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    await event.respond(
        "👋 Welcome to **WordRush Bot**!\n\n"
        "Play word guessing challenges with your friends.\n"
        "Use /new to start a game!"
    )