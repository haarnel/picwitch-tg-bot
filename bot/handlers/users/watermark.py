from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.message import Message
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from bot.states import MainState, WatermarkState
from bot.keyboards.default import main_menu_kb

from bot.api import client


async def watermark_choice(message: types.Message, state: FSMContext):
    message_text = message.text

    if "загрузить" in message_text.lower():
        await WatermarkState.UPLOAD.set()
        await message.answer(
            text="Пришлите мне фото как документ в формате .png (обязательно): ",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await MainState.MENU_SHOW.set()
        await message.answer(text="Выберите меню: ", reply_markup=main_menu_kb)


async def watermark_receive(message: types.Message, state: FSMContext):
    if message.document:
        w_file_id = message.document.file_id
    elif message.photo:
        w_file_id = message.photo[-1].file_id

    state_data = await state.get_data()
    original_photo = state_data["file_id"]
    im_result = await client.watermark(original_photo, w_file_id)
    await message.reply_photo(im_result, reply_markup=main_menu_kb)

    await state.finish()
    await MainState.MENU_SHOW.set()

    await state.update_data(file_id=original_photo)
