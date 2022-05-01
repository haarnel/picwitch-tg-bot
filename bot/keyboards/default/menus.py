from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✨ Фильтры"),
            KeyboardButton(text="⚙  Сжатие"),
            KeyboardButton(text="🗺 Метаданные"),
        ],
        [
            KeyboardButton(text="👓 Заблюрить"),
            KeyboardButton(text="🖼 Миниатюра"),
            KeyboardButton(text="🎨 Палитра"),
        ],
        [
            KeyboardButton(text="🔁 Перевернуть"),
            KeyboardButton(text="🌀 Отзеркалить"),
            KeyboardButton(text="🔆 Яркость"),
        ],
        [KeyboardButton(text="♒ Watermark")],
        [
            KeyboardButton(text="❌ Отменить"),
        ],
    ],
    resize_keyboard=True,
    row_width=2,
)

filters_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1. Contour"),
            KeyboardButton(text="2. Sharpen"),
            KeyboardButton(text="3. Detail"),
            KeyboardButton(text="4. Smooth"),
            KeyboardButton(text="5. Edges"),
        ],
        [
            KeyboardButton(text="6. Emboss"),
            KeyboardButton(text="7. Lighten"),
            KeyboardButton(text="8. Darken"),
            KeyboardButton(text="9. Grayscale"),
            KeyboardButton(text="10. Invert"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=3,
)


blur_ranges_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="5"),
            KeyboardButton(text="10"),
        ],
        [
            KeyboardButton(text="15"),
            KeyboardButton(text="20"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=2,
)

image_info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔍 Получить информацию"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)

rotate_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"{i}") for i in range(90, 360, 90)],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=3,
)


mirror_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌀 Отзеркалить изображение"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)

palette_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎨 Получить цветовую палитру"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)

brightness_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"{round(i * 0.1, 1)}") for i in range(11, 21)],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=10,
)


thumbnail_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📐 Задать параметры для миниатюры"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)


confirm_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🏁 Получить результат"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)


compress_jpeg_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"{i}") for i in range(10, 110, 10)],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=2,
)

watermark_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"📁 Загрузить логотип"),
        ],
        [KeyboardButton(text="🔙 Назад")],
    ],
    resize_keyboard=True,
    row_width=1,
)
