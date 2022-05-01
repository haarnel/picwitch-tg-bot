from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb, rotate_kb

from bot.api import client


async def rotate_choice(message: types.Message, state: FSMContext):
    rotate_deg = message.text.strip()
    allowed_radius = ["90", "180", "270"]
    if rotate_deg in allowed_radius:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        im_result = await client.rotate_image(file_id, rotate_deg)
        await message.reply_photo(im_result)
    else:
        await MainState.MENU_SHOW.set()
        await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
