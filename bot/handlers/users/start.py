from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from bot.states import MainState


async def cmd_start(message: types.Message, state: FSMContext):
    message_text = "👋 Приветствую тебя, пришли мне любую фотографию и мы посмотрим, что можно с ней сделать ✨"
    await message.answer(text=message_text, reply_markup=ReplyKeyboardRemove())
    current_state = await state.get_state()
    if not current_state:
        await MainState.STARTED.set()
    else:
        await state.finish()
