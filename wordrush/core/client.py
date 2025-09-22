from telethon import TelegramClient
from os import environ 
from dotenv import load_dotenv

load_dotenv()

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]

wordrush = TelegramClient("wordrush", api_id, api_hash).start(bot_token=bot_token)
wordrush.start()