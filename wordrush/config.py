valid_difficulties = ["easy", "medium", "hard", "extreme"]
is_playing = {}
current_difficulty = {}
guess_history = {}

user_log_caption="Congratulations.\nNew user started **WordRush.**\n\nUsername: @{username}\nName: {full_name}\nId: {sender_id}"
group_log_caption="Congratulations.\n**WordRush** has been added to one more group.\n\nusername: @{username}\nName: {full_name}\nId: {chat_id}"

start_caption = "**Hey there** {mention},\n\nWelcome to **[WordRushBot](https://t.me/wordrush_bot)**,\n\n**The ultimate word challange —— fun, fast, and competitive With leaderboard, only on Telegram!**\n\n1. Use **/new** to start a game. Add me to a group with admin permission to play with your friends.\n\n**Click in the Help Menu button below To get more information, How to play and about commands.**"

start_caption_2 = "**Welcome back! to [WordRushBot](https://t.me/wordrush_bot)**,\n\n**The ultimate word challange —— fun, fast, and competitive With leaderboard, only on Telegram!**\n\n1. Use **/new** to start a game. Add me to a group with admin permission to play with your friends.\n\n**Click in the Help Menu button below To get more information, How to play and about commands.**"

help_menu_caption = "**WordRush's Help menu**\n\n Choose the category you want to help with **WordRush**\n\nAny problem ask your doubt at [WordRush Play & Report](https://t.me/astrabotz_chat)"

how_to_play_caption = "**🕹️ How to Play Word Rush**\n\n1️⃣ You have to guess a secret word.\n- 🟢 Easy → 4-letter word (example: game)\n- 🟡 Medium → 5-letter word (example: apple)\n- 🔴 Hard → 8-letter word (example: football)\n- ⚫ Extreme → 10-letter word (example: basketball)\n\n2️⃣ After every guess, you will get hints:\n- 🟩 Green = Correct letter in the right place.\n- 🟨 Yellow = Correct letter but in the wrong place.\n- 🟥 Red = Letter not in the word.\n\n3️⃣ You can make up to 30 guesses. The game continues until someone finds the correct word.\n\n4️⃣ The first person who guesses the word correctly is the winner 🏆.\n\n5️⃣ Winners get points based on difficulty. More difficult = more points.\n\n6️⃣ All points are saved in the Leaderboard.\n\n💡 Tip: Use the hints smartly and try to win with fewer guesses to earn more points!"

commands_menu_caption = "**📖 Word Rush Commands**\n\n🎮 /new **(or /new easy|medium|hard|extreme)** → Start a new game. You can also set difficulty while starting.\n\n🛑 /end → End the current game **(Group Admins only).**\n\n⚙️ /difficulty **(easy|medium|hard|extreme)** → Change difficulty for the current chat **(Group Admins only).**\n\n🏆 /leaderboard → Show the global and group leaderboard.\n\n❓ /help → Show the help menu."