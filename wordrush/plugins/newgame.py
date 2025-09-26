from telethon import events
from wordrush.core.client import wordrush
from wordrush.core.database import difficulty_col
from wordrush.config import valid_difficulties, is_playing
from wordrush.misc.getword import get_word

@wordrush.on(events.NewMessage(pattern=r"(?i)\/new(?:\s+(.+))?"))
async def newgame(event):
    chat_id = event.chat_id
    if is_playing[chat_id]:
        return await event.respond("There is already a game in progress in this chat. Use **/end** to end the current game.")
    difficulty = event.pattern_match.group(1)
    if difficulty:
        difficulty = difficulty.strip().lower()
        if difficulty not in valid_difficulties:
            return await event.reply(f"**{difficulty}** is not valid difficult!\n\n**Available Difficulty's:**\n\n`easy` - To give 3-4 latter word.\n`medium` - To give 5 latter word.\n`hard` - To give 6-8 latter word.\n`extreme` - To give 9-12 latter word.")
    else:
        if event.is_private:
            sender = await event.get_sender()
            sender_id = sender.id
            if not difficulty:
                doc = difficulty_col.find_one({"chat_id": sender_id})
                difficulty = doc["difficulty"] if doc and "difficulty" in doc else "medium"
        
        if not difficulty:
            doc = difficulty_col.find_one({"chat_id": chat_id})
            difficulty = doc["difficulty"] if doc and "difficulty" in doc else "medium"
    if difficulty == "easy":
        latters = "3-4"
    if difficulty == "medium":
        latters = "5"
    if difficulty == "hard":
        latters = "6-8"
    if difficulty == "extreme":
        latters = "9-10"
    await event.respond(f"**Game started!**\nDifficulty set to **{difficulty}** \n\nGuess the **{latters} latters word!**")
    is_playing[chat_id] = get_word(difficulty)