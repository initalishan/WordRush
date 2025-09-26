from telethon import events
from wordrush.core.client import wordrush
from wordrush.config import is_playing
from wordrush.utils.buttons import play_again_button
from wordrush.plugins.newgame import newgame

wordrush.on(events.NewMessage)
async def guess(event):
    user = await event.get_sender()
    try:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
    except Exception:
        mention = "Anonymous"
    chat_id = event.chat_id
    if not is_playing[chat_id]:
        return
    if event.message.media:
        return
    word = is_playing[chat_id].lower()
    guess = str(event.text).lower()
    if not len(guess) == len(word):
        return
    status = []
    for i in range(len(word)):
        if not word[i] == guess[i]:
            if i == 0:
                status.append("🟩")
            else:
                status.append(" 🟩")
        elif guess[i] in word:
            if i == 0:
                status.append("🟨")
            else:
                status.append(" 🟨")
        else:
            if i == 0:
                status.append("🟥")
            else:
                status.append(" 🟥")
    if word == guess:
        await event.respond(f"Congratulations dear **{mention} 🎉**\n\nYou guessed the currect word! Word was **{word.upper()}**", buttons=play_again_button)
        del is_playing[chat_id]
    else:
        await event.respond(" ".join(status), "-", guess.upper())
        
@wordrush.on(events.CallbackQuery(data=b"play_again"))
async def call_newgame(event):
    await newgame(event)
