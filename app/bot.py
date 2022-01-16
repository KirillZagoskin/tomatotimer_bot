import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher

from config import TOKEN, YEAR, MINUTE
# from database import database as db, cache
from app.dialogs import msg
import app.service as s 


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Обработка команды /start. Установка команд боту. Вывод текста"""
    await s.set_commands(bot)
    await message.answer(msg.start_text.format(name=message.from_user.first_name))


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    """Обработка команды /help. Вывод текста"""
    await message.answer(msg.help_test)


@dp.message_handler()
async def unknown_message(message: types.Message):
    """Ответ на любое неожиданное сообщение"""
    await message.answer(msg.unknown_text)


async def on_shutdown(dp):
    logging.warning('Shutting down....')
