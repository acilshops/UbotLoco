import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "6681594954").split()))

API_ID = int(os.getenv("API_ID", "24686094"))

API_HASH = os.getenv("API_HASH", "67d654b9f81bf142f111ffdad7c42348")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8493018603:AAEvahyle-F7ZjutoZrvvg_UCFB9Mc0ialA")

OWNER_ID = int(os.getenv("OWNER_ID", "6681594954"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://yasrilpujianto38_db_userbot:AJDU2iX6QcTkHZHM@cluster0.erlp6tz.mongodb.net/?appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))
