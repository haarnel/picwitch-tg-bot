from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb, filters_menu_kb

from bot.api import client


async def filter_choice(message: types.Message, state: FSMContext):
    filter_func = message.text
    filter_func = filter_func.split(".")[-1].strip().lower()
    available_filters = [
        "edges",
        "emboss",
        "lighten",
        "darken",
        "contour",
        "sharpen",
        "detail",
        "smooth",
        "grayscale",
        "invert",
    ]
    if filter_func in available_filters:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        im_result = await client.apply_filter(file_id, filter_func)
        await message.reply_photo(im_result)
    elif "назад" in filter_func:
        await MainState.MENU_SHOW.set()
        await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
