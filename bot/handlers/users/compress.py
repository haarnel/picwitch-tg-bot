from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb

from bot.api import client


async def compress_choice(message: types.Message, state: FSMContext):
    message_text = message.text
    if "назад" in message_text.lower():
        await MainState.MENU_SHOW.set()
        await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
    else:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        # file_ext = state_data["file_ext"]
        im_result = await client.compress(file_id, message_text.strip())
        await message.reply_document(im_result)

    # await state.finish()

    # await state.update_data(file_id=file_id)
