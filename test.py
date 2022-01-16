import unittest
import aiohttp
from unittest import IsolatedAsyncioTestCase

from app import bot


class TestBot(IsolatedAsyncioTestCase):
    async def test_bot_auth(self):
        bot.bot._session = aiohttp.ClientSession()
        bot_info = await bot.bot.get_me()
        await bot.bot._session.close()
        self.assertEqual(bot_info["username"], "tomatotimer_bot")


if __name__ == '__main__':
    unittest.main()
