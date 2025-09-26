from telethon import events 
from wordrush.core.client import wordrush
from wordrush.core.database import difficulty_col
from wordrush.config import valid_difficulties
from wordrush.config import us_playing

@wordrush.on(events.NewMessage(pattern=r"(?i)\/difficulty\s(.+)"))
async def difficulty(event):
    difficulty = event.pattern_match.group(1)
    if not difficulty:
        return await event.reply("**Valid usage**\n\n`/difficulty easy`\n**Like this!**\n\n**Available difficulty:**\n")
    user = await event.get_sender()
    chat = await event.get_chat()
    rights = await wordrush.get_permissions(chat.id, user.id)
    if not rights.is_admin:
        await event.reply("You must be an admin to use this.")
        return
    if is_playing[event.chat_id]:
        return await event.respond("There is already a game in progress in this chat. You can't change the difficulty.\n\nTo stop game hit **/end**")
    if difficulty:
        difficulty = difficulty.strip().lower()
        if difficulty not in valid_difficulties:
            return await event.respond(f"**{difficulty}** is not valid difficult!\n\n**Available Difficulty's:**\n\n`easy` - To give 4 latter word.\n`medium` - To give 5 latter word.\n`hard` - To give 8 latter word.\n`extreme` - To give 10 latter word.")
        else:
            difficulty_col.update_one({"chat_id": event.chat_id}, {"$set": {"difficulty": difficulty}}, upsert=True)
            await event.respond(f"difficulty successfully set to **{difficulty}**")