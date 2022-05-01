from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb

from bot.api import client


async def brightness_choice(message: types.Message, state: FSMContext):
    factor = message.text.strip()
    allowed_factor = [str(round(x * 0.1, 1)) for x in range(11, 21)]
    if factor in allowed_factor:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        im_result = await client.brightness(file_id, factor)
        await message.reply_photo(im_result)
    else:
        await MainState.MENU_SHOW.set()
        await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
