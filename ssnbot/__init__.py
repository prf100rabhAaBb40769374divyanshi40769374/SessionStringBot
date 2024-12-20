import os
import re
import logging
import logging.config
from dotenv import load_dotenv

load_dotenv(override=True)

pattern = re.compile(r"^.\d+$")

# vars
APP_ID = os.environ.get("APP_ID", "26598255")
API_HASH = os.environ.get("API_HASH", "2851fb6ab1bdcd0fcaf768dfcb923ffb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7575561551:AAF4FpCmHFKD6dTfXXscoPihbpOnwdD-HbQ")
DB_URL = os.environ.get("DB_URL", "mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(os.environ.get('OWNER_ID', "7400823450"))
MUST_JOIN = os.environ.get("MUST_JOIN", "PROFESSORxBOTS")
ADMINS = [
    int(user) if pattern.search(user) else user
    for user in os.environ.get("ADMINS", "").split()
] + [OWNER_ID]


# logging Conf
logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
