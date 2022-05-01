from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb

from bot.api import client


async def blur_choice(message: types.Message, state: FSMContext):
    blur_radius = message.text.strip()
    allowed_radius = ["5", "10", "15", "20"]
    if blur_radius in allowed_radius:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        im_result = await client.apply_blur(file_id, blur_radius)
        await message.reply_photo(im_result)
    else:
        await MainState.MENU_SHOW.set()
        await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
