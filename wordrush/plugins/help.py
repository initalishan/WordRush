from wordrush.core.client import wordrush
from telethon import events
from wordrush.config import start_caption, start_caption_2, help_menu_caption, commands_menu_caption, how_to_play_caption
from wordrush.utils.buttons import start_buttons, start_group_buttons, help_menu_buttons, back_to_help_buttons

async def help_menu(event):
    await event.edit(help_menu_caption, buttons=help_menu_buttons)
    
@wordrush.on(events.CallbackQuery(data=b"help_menu"))
async def help_menu_call_with_button(event):
    await help_menu(event)

@wordrush.on(events.NewMessage(pattern=r"(?i)\/help"))
async def help_menu_call_with_command(event):
    await help_menu(event)
    
@wordrush.on(events.CallbackQuery(data=b"back_to_start"))
async def back_to_start(event):
    await event.edit(start_caption_2, buttons=start_buttons)
    
@wordrush.on(events.CallbackQuery(data=b"back_to_help"))
async def back_to_help(event):
    await event.edit(help_menu_caption, buttons=help_menu_buttons)

@wordrush.on(events.CallbackQuery(data=b"how_to_play"))
async def how_to_play(event):
    await event.edit(how_to_play_caption, buttons=back_to_help_buttons)
@wordrush.on(events.CallbackQuery(data=b"commands_menu"))
async def commands_menu(event):
    await event.edit(commands_menu_caption, buttons=back_to_help_buttons)