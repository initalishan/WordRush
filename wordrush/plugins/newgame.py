from telethon import events
from wordrush.core.client import wordrush
from wordrush.core.database import difficulty_col

@wordrush.on(events.NewMessage(pattern=r"(?i)\/new(?:@[\w]+)?(?:\s+(.+))?"))
async def newgame(event):
    difficulty = event.pattern_match.group(1)
    if difficulty == "easy":
        difficulty = "easy"
    if difficulty == "medium":
        difficulty = "medium"
    if difficulty == "hard":
        difficulty = "hard"
    if difficulty == "extreme":
        difficulty = "extreme"
    if difficulty:
        return await event.reply(f"{difficulty} is not valid, **Available Difficult's**\n`easy` - To give 3-4 latter word.\n`medium` To give 5 latter word.\n`hard` - T give 6-8 latter word.\n`extreme` - To give 9-12 latter word.")
    if event.is_private:
        sender = await event.get_sender()
        sender_id = sender.id
        if not difficulty:
            doc = difficulty_col.find_one({"chat_id": sender_id})
            difficulty = doc["difficulty"] if doc and "difficulty" in doc else "medium"
        
    chat_id = event.chat_id
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
    await event.respond(f"**Game started!**\nDifficulty set to**{difficulty}** \n\nGuess the **{latters} latters word!**")
    