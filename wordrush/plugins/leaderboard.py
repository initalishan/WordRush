from wordrush.core.client import wordrush
from telethon import events
from wordrush.core.database import users_pts_col


@wordrush.on(events.NewMessage(pattern=r"(?i)\/leaderboard"))
async def leaderboard(event):
    top_users = users_pts_col.find().sort("points", -1).limit(20).to_list(length=20)
    
    if not top_users:
        return await event.respond("No players found in leaderboard yet.")
        
    leaderboard_text = "🏆 **Leaderboard (Top 20)** 🏆\n\n"
    medals = ["🥇", "🥈", "🥉"]

    for idx, user in enumerate(top_users, start=1):
        user_id = user.get("user_id")
        points = user.get("points", 0)

        try:
            tg_user = await event.client.get_entity(user_id)
            name = tg_user.first_name or "Unknown"
        except Exception:
            name = "Unknown"

        mention = f"[{name}](tg://user?id={user_id})"

        if idx <= 3:
            leaderboard_text += f"{medals[idx-1]} {mention} — `{points} Points`\n"
        else:
            leaderboard_text += f"**{idx}. {mention}** → `{points} Points`\n"
        
    await event.respond(leaderboard_text, parse_mode="md")