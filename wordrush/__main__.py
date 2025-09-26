print("Loading core system..")
from wordrush.core.client import wordrush
import importlib
from asyncio import get_event_loop
from os import listdir
from wordrush.Logs import logs

async def main():
    print("Starting Client..")
    print("Loading Plugins..")
    import_plugins()
    print("Plugin loaded!")
    print("BOT STARTED.")
    await wordrush.run_until_disconnected()
    
def import_plugins():
    path = "wordrush/plugins"
    for file in listdir(path):
        if file.endswith(".py") and not file.startswith("__"):
            importlib.import_module(f"wordrush.plugins.{file[:-3]}")
            print(f"{file[:-3]} plugin loaded succesfully.")
            
loop = get_event_loop()
loop.run_until_complete(main())