from wordrush.core.client import wordrush
from telethon import events, Button
from wordrush.core.database import users_pts_col
from datetime import datetime, timedelta


def get_leaderboard_buttons(chat_id):
    return [
        [Button.inline("🌍 Global", data="lb_global")],
        [Button.inline("💬 This Chat", data=f"lb_chat_{chat_id}")],
        [
            Button.inline("📅 Today", data="lb_today"),
            Button.inline("🗓 Weekly", data="lb_weekly"),
            Button.inline("📆 Monthly", data="lb_monthly"),
        ],
    ]


async def fetch_leaderboard(event, filter_query, per_chat=False):
    # Choose field based on global or per-chat
    sort_field = "chat_points" if per_chat else "points"
    top_users = list(users_pts_col.find(filter_query).sort(sort_field, -1).limit(20))

    if not top_users:
        return "No players found for this leaderboard yet."

    leaderboard_text = "🏆 **Leaderboard (Top 20)** 🏆\n\n"
    medals = ["🥇", "🥈", "🥉"]

    for idx, user in enumerate(top_users, start=1):
        user_id = user.get("user_id")
        points = user.get(sort_field, 0)

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

    return leaderboard_text


@wordrush.on(events.NewMessage(pattern=r"(?i)\/leaderboard"))
async def leaderboard(event):
    leaderboard_text = await fetch_leaderboard(event, {}, per_chat=False)
    await event.respond(
        leaderboard_text,
        buttons=get_leaderboard_buttons(event.chat_id),
        parse_mode="md"
    )


@wordrush.on(events.CallbackQuery(pattern=b"lb_(.*)"))
async def leaderboard_cb(event):
    query = event.data.decode().split("_", 1)[1]
    now = datetime.utcnow()
    filter_query = {}
    per_chat = False

    if query == "global":
        filter_query = {}
        per_chat = False
    elif query.startswith("chat"):
        chat_id = int(query.split("_")[1])
        filter_query = {"chat_id": chat_id}
        per_chat = True
    elif query == "today":
        start = datetime(now.year, now.month, now.day)
        filter_query = {"last_played": {"$gte": start}}
    elif query == "weekly":
        start = now - timedelta(days=7)
        filter_query = {"last_played": {"$gte": start}}
    elif query == "monthly":
        start = now - timedelta(days=30)
        filter_query = {"last_played": {"$gte": start}}

    leaderboard_text = await fetch_leaderboard(event, filter_query, per_chat=per_chat)
    await event.edit(
        leaderboard_text,
        buttons=get_leaderboard_buttons(event.chat_id),
        parse_mode="md"
    )