from aiogram.types import file
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from bot.states.states import SizeState
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb, confirm_kb
from aiogram.utils.markdown import hbold, italic

from bot.api import client
from bot.states import SizeState


async def thumbnail_choice(message: types.Message, state: FSMContext):
    message_text = message.text.strip()
    if not "назад" in message_text:
        await SizeState.WIDTH.set()
        text = f"Пришлите мне желаемую {italic('ширину')} в px: "
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


async def thumbnail_choice_width(message: types.Message, state: FSMContext):
    width = message.text.strip()
    await state.update_data(width=width)
    await SizeState.HEIGHT.set()
    await message.answer(text=f"Отлично. Укажите {italic('высоту')} в px: ")


async def thumbnail_choice_height(message: types.Message, state: FSMContext):
    height = message.text.strip()
    await state.update_data(height=height)
    await SizeState.READY.set()
    await message.answer(text=f"Выберите действие: ", reply_markup=confirm_kb)


async def thumbnail_get_result(message: types.Message, state: FSMContext):
    message_text = message.text
    state_data = await state.get_data()
    file_id = state_data["file_id"]
    if "назад" not in message_text.lower():
        im_result = await client.thumbnail(**state_data)
        await message.reply_photo(im_result, reply_markup=main_menu_kb)
        await state.finish()
        await MainState.MENU_SHOW.set()

    await state.update_data(file_id=file_id)
