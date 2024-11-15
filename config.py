import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "4993786"))
API_HASH = getenv("API_HASH")

ASS_HANDLER = list(getenv("ASS_HANDLER", "/").split())
BOT_TOKEN = getenv("BOT_TOKEN")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID"))
MONGO_DB_URI = getenv("MONGO_DB_URI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1063334882").split()))

PING_IMG = getenv("PING_IMG", "https://graph.org//file/389a372e8ae039320ca6c.png")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ALONExSUPPORT")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/itz_Xdpranay")

STRING_SESSION = getenv("STRING_SESSION", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1063334882").split()))
