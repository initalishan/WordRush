from telethon import events
from wordrush.core.client import wordrush
from wordrush.config import is_playing, current_difficulty, guess_history
from wordrush.utils.buttons import play_again_button
from wordrush.plugins.newgame import start_newgame
from wordrush.core.database import users_pts_col
import re

with open("word.txt") as f:
    valid_words = set(w.strip().lower() for w in f if w.strip())
    
@wordrush.on(events.NewMessage)
async def guess(event):
    if not event.is_private and event.is_reply:
        return
    chat_id = event.chat_id
    if not chat_id in is_playing:
        return
    if event.message.media:
        return
    text = event.text.strip()
    if not re.fullmatch(r"[A-Za-z]+", text):
        return
    guess = text.lower()
    word = is_playing[chat_id].lower()
    if not len(guess) == len(word):
        return
    if guess not in valid_words:
        return await event.reply(f"**{guess}** is not a valid word.")
    user = await event.get_sender()
    try:
        mention = f"[{user.first_name}](tg://user?id={user.id})"
    except Exception:
        mention = "Anonymous"
    status = []
    for i in range(len(word)):
        if word[i] == guess[i]:
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
    if chat_id not in guess_history:
        guess_history[chat_id] = []
    already_guessed = any(guess.upper() in entry for entry in guess_history[chat_id])
    if not already_guessed:
        guess_history[chat_id].append(f"{''.join(status)} - **{guess.upper()}**")
    else:
        await event.respond(f"**{guess}** is already guessed.")
    if word == guess:
        full_history = "\n".join(guess_history[chat_id])
        difficulty = current_difficulty[chat_id]
        if difficulty == "easy":
            base_points = 20
        elif difficulty == "medium":
            base_points = 40
        elif difficulty == "hard":
            base_points = 70
        elif difficulty == "extreme":
            base_points = 100
        else:
            base_points = 10 
        turn_no = len(guess_history[chat_id])
        points = max(int(base_points * (0.9 ** (turn_no - 1))), base_points // 4)
        await event.respond(f"Congratulations**{mention}**\nYou earned **{points} Points**\n\nYou guessed the currect word! \nWord was **{word.upper()}**", buttons=play_again_button)
        users_pts_col.update_one(
    {"user_id": user.id},
    {"$inc": {"points": points}},
    upsert=True
)
        del is_playing[chat_id]
        del guess_history[chat_id]
    else:
        full_history = "\n".join(guess_history[chat_id])
        await event.respond(f"{full_history}")
        
@wordrush.on(events.CallbackQuery(data=b"play_again"))
async def call_newgame(event):
    chat_id = event.chat_id
    await start_newgame(event, current_difficulty[chat_id])