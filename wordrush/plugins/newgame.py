from telethon import events
from wordrush.core.client import wordrush
from wordrush.core.database import difficulty_col
from wordrush.config import valid_difficulties, is_playing, current_difficulty
from wordrush.misc.getword import get_word

async def start_newgame(event, difficulty=None):
    chat_id = event.chat_id
    if chat_id in is_playing:
        return await event.respond("There is already a game in progress in this chat. Use **/end** to end the current game.")
    if difficulty:
        if difficulty not in valid_difficulties:
            return await event.reply(
                f"**{difficulty}** is not a valid difficulty!\n\n"
                "**Available Difficulties:**\n"
                "`easy` - 4 letters\n"
                "`medium` - 5 letters\n"
                "`hard` - 8 letters\n"
                "`extreme` - 10 letters"
            )
    else:
        if event.is_private:
            sender_id = (await event.get_sender()).id
            doc = difficulty_col.find_one({"chat_id": sender_id})
            difficulty = doc["difficulty"] if doc and "difficulty" in doc else "medium"
        else:
            doc = difficulty_col.find_one({"chat_id": chat_id})
            difficulty = doc["difficulty"] if doc and "difficulty" in doc else "medium"

    latters_map = {
        "easy": "4",
        "medium": "5",
        "hard": "8",
        "extreme": "10"
    }
    latters = latters_map.get(difficulty, "?")

    await event.respond(
        f"**Game started!**\nDifficulty set to **{difficulty}**\n\n"
        f"Guess the **{latters} letters word!**"
    )
    current_difficulty[chat_id] = difficulty
    is_playing[chat_id] = get_word(difficulty)


@wordrush.on(events.NewMessage(pattern=r"(?i)\/new(?:\s+(.+))?"))
async def newgame(event):
    difficulty = event.pattern_match.group(1)
    if difficulty:
        difficulty = difficulty.strip().lower()
        await start_newgame(event, difficulty)
    else:
        await start_newgame(event, None)