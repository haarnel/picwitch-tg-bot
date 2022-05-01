from bot.states.states import MainState
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.keyboards.default import main_menu_kb


async def recive_photo(message: types.Message, state: FSMContext):
    if message.document:
        file_id = message.document.file_id
        # TODO: detect image type for photo.
        file_ext = message.document.file_name
    elif message.photo:
        file_id = message.photo[-1].file_id

    async with state.proxy() as data:
        data["file_id"] = file_id
        # data["file_ext"] = file_ext

    await MainState.FILE_UPLOADED.set()

    await message.answer(text="Вот что я умею: ", reply_markup=main_menu_kb)
    await MainState.MENU_SHOW.set()
