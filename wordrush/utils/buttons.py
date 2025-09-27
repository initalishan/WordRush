from telethon import Button

play_again_button = [Button.inline("Play Again", data=b"play_again")]
    
start_buttons = [
    [Button.url("Add me to your chat", "http://t.me/wordrush_bot?startgroup=botstart")],
    [Button.inline("Help Menu", data=b"help_menu")],
    [
        Button.url("Play & Report", "https://t.me/astrabotz"),
        Button.url("Updates", "https://t.me/astrabotz")
        ]
    ]
    
start_group_buttons = [
    [Button.url("Start me", "https://t.me/WordRush_Bot?start=_tgr_s11d9dgxZmFl")],
    [
        Button.url("Play & Report", "https://t.me/astrabotz"),
        Button.url("Updates", "https://t.me/astrabotz")
        ]
    ]
    
help_menu_buttons = [
    [Button.inline("How to play ❓", data=b"how_to_play")],
    [Button.inline("Commands 📚", data=b"commands_menu")],
    [Button.inline("Back to start", data=b"back_to_start")]
    ]
back_to_help_buttons = [
    [Button.inline("Back to help 📚", data=b"back_to_help")]
    ]