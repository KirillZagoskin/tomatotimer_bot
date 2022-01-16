from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton, \
                          BotCommand
from emoji import emojize

from config import MINUTE
# from database import cache, database as db
from app.dialogs import msg


async def set_commands(bot):
    commands = [
        BotCommand(command="start", description="Запуск"),
        BotCommand(command="help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)
