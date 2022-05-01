from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb

from bot.api import client


async def mirror_choice(message: types.Message, state: FSMContext):
    message_text = message.text
    if "назад" in message_text.lower():
        pass
    else:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        im_result = await client.mirror(file_id)
        await message.reply_photo(im_result)

    await MainState.MENU_SHOW.set()
    await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
