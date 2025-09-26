from telethon import events 
from wordrush.core.client import wordrush
from wordrush.core.database import difficulty_col
from wordrush.config import valid_difficulties

@wordrush.on(events.NewMessage(pattern=r"(?i)\/difficulty\s(.+)"))
async def difficulty(event):
    difficulty = event.pattern_match.group(1)
    if not difficulty:
        return await event.reply("**Valid usage**\n\n`/difficulty easy`\n**Like this!**\n\n**Available difficulty:**\n")
    elif difficulty.strip().lower in valid_difficulties:
        difficulty_col.update_one({"chat_id": event.chat_id}, {"$set": {"difficulty": difficulty.strip().lower()}}, upsert=True)
        await event.respond(f"difficulty successful ly set to ***{difficulty.strip().lower()}**")
    else:
        return await event.respond("This difficulty **not available**\n\n**Valid difficulties:***\n`easy` - To give 3-4 latter word.\n`medium` - To give 5 latter word.\n`hard` - To give 6-8 latter word.\n`extreme` - To give 9-12 latter word.")
        