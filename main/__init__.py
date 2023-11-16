#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 20595111
API_HASH = "16cbd8f20f65c475d0912a2447b71c48"
BOT_TOKEN = "6223085586:AAFtVYiQ0AfYMQkJpc02_QFq6YehmjJUlUo"
SESSION = "BQE6QacAW4Fs0lNl2a3dW8ujEFcEuMW3KUXLG-Om4GvfuFtYXZKbN0CqDls7Sudsby8asItykhhXFWJe3lh5OeuNoQEt5Fsm15GDnXZx0Ha48sWBuDc3NydMEOjL9s82xISxT__iBY0dyWpuOF9Yvs_HhG8TVE8JnfC-b03DmEO-XAWeuSJL6FegZDEYH2cicV9SHkDI0jDpn5thiutgrME83WzAkOsz8_LBr1DQQrvqsqvQFxllSYIqsfEKTA34kIwTPWzMOLUxJTB4iTldTeBo0xXzEdckfWfV-8V66U_gLcceheFV18fqiM93j_m_fagTnx9T1zJFU1eiWSWFoPsekAj6egAAAAFvXAxLAA"
FORCESUB = "defenderofthemultiverse"
AUTH = 1197918807
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
