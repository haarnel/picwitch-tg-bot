from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from bot.states import MainState
from bot.keyboards.default import (
    filters_menu_kb,
    main_menu_kb,
    blur_ranges_kb,
    image_info_kb,
    rotate_kb,
    palette_kb,
    mirror_kb,
    brightness_kb,
    thumbnail_kb,
    compress_jpeg_kb,
    watermark_kb,
)


async def menu_choice(message: types.Message, state: FSMContext):
    message_text = message.text.strip().lower()

    if "фильтры" in message_text:
        await MainState.FILTERS.set()
        await message.answer(
            text="Какой фильтр вы хотите применить: ",
            reply_markup=filters_menu_kb,
        )

    elif "сжатие" in message_text:
        await MainState.COMPRESS.set()
        await message.answer(
            text="Укажите желаемое качество после обработки (поддерживается только jpeg): ",
            reply_markup=compress_jpeg_kb,
        )

    elif "заблюрить" in message_text:
        await MainState.BLUR.set()
        await message.answer(
            text="Выберить радиус размытия: ",
            reply_markup=blur_ranges_kb,
        )
    elif "метаданные" in message_text:
        await MainState.IMAGE_INFO.set()
        await message.answer(
            text="Нажмите кнопку ниже для получения информации: ",
            reply_markup=image_info_kb,
        )

    elif "перевернуть" in message_text:
        await MainState.ROTATE.set()
        await message.answer(
            text="Выбериде градус для поворота изображения: ",
            reply_markup=rotate_kb,
        )

    elif "отзеркалить" in message_text:
        await MainState.MIRROR.set()
        await message.answer(
            text="Нажмите кнопку ниже чтобы отзеркалить изображение: ",
            reply_markup=mirror_kb,
        )

    elif "палитра" in message_text:
        await MainState.PALETTE.set()
        await message.answer(
            "Нажмите кнопку ниже для получения палитры:", reply_markup=palette_kb
        )

    elif "яркость" in message_text:
        await MainState.BRIGHTNESS.set()
        await message.answer(
            "Выберите фактор увеличения яркости: ", reply_markup=brightness_kb
        )

    elif "миниатюра" in message_text:
        await MainState.THUMBNAIL.set()
        await message.answer(
            "Генерация миниатюры из изображения (аватарка): ", reply_markup=thumbnail_kb
        )

    elif "watermark" in message_text:
        await MainState.WATERMARK.set(),
        await message.answer(
            "Поместить водяной знак на вашу фотографию: ",
            reply_markup=watermark_kb,
        )

    elif "отменить" in message_text:
        await state.finish()
        await message.answer(
            text="Выберите команду /start, чтобы начать заново",
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await message.answer(text="Выберите из меню: ", reply_markup=main_menu_kb)
