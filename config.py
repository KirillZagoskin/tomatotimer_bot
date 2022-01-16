import os
import logging


logging.basicConfig(level=logging.INFO)

BOT_VERSION = 0.1
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

BOT_DB_NAME = ""

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

MINUTE = 60
YEAR = 60*60*24*366
