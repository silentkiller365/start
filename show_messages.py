import asyncio,logging,os
from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
load_dotenv(override=True)

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
session_string = input("Enter StringSession: ")

client = TelegramClient(StringSession(session_string), API_ID, API_HASH).start()

@client.on(events.NewMessage(pattern=".id"))
async def handler(event):
    await event.reply("Chat id: `{}`".format(event.chat.id))
@client.on(events.NewMessage)
async def handler(event):
    print(event.message.message)
client.run_until_disconnected()