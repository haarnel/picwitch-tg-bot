from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.states import MainState
from bot.keyboards.default import main_menu_kb, filters_menu_kb

from bot.api import client


async def image_info_choice(message: types.Message, state: FSMContext):
    text = message.text.split()[-1].lower()
    if text == "назад":
        await MainState.MENU_SHOW.set()
    else:
        state_data = await state.get_data()
        file_id = state_data["file_id"]
        result = await client.get_image_info(file_id)
        params = ""
        latitude = None
        longitude = None
        for key, value in result.items():
            if key == "GPSLatitude":
                latitude = float(value.split()[0])
            if key == "GPSLongitude":
                longitude = float(value.split()[0])
            params += f"{key} : {value}\n"

        await message.reply(text=params)

        if latitude and latitude:
            await message.reply_location(latitude=latitude, longitude=longitude)

        await MainState.MENU_SHOW.set()

    await message.answer("Выберите меню: ", reply_markup=main_menu_kb)
