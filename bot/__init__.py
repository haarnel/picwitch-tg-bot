import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import Executor

from bot.handlers import users
from bot.utils.config import Config
from bot.utils.commands import set_default_commands, notify_admins

from bot.api import client

bot = Bot(token=Config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
mstorage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=mstorage)


async def on_startup(dp: Dispatcher):
    await client.check_status()
    await set_default_commands(dp)
    await notify_admins(dp, status="запущен")


async def on_shutdown(dp: Dispatcher):
    await notify_admins(dp, status="остановлен")
    await dp.bot.close()
    await client.session.close()


def create_bot() -> Executor:
    loop = asyncio.get_event_loop()
    executor = Executor(dispatcher=dp, loop=loop)
    executor.on_startup(on_startup)
    executor.on_shutdown(on_shutdown)

    users.setup(dp)

    return executor
