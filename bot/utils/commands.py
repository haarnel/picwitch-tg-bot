from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from bot.utils.config import Config


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать работу с ботом"),
            types.BotCommand("help", "Информация по работе с ботом"),
        ]
    )


async def notify_admins(dp: Dispatcher, status: str) -> None:
    bot = await dp.bot.get_me()
    message = "Привет @{admin_username}, бот @{bot_username} был успешно {status}."
    for admin in Config.ADMINS:
        chat = await dp.bot.get_chat(chat_id=admin)
        await dp.bot.send_message(
            chat_id=admin,
            text=message.format(
                admin_username=chat.username,
                bot_username=bot.username,
                status=status,
            ),
            reply_markup=ReplyKeyboardRemove(),
        )
