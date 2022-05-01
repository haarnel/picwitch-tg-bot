from bot.states.states import WatermarkState
from bot.handlers.users.filters import filter_choice
from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, state

from bot.states import MainState, SizeState
from .start import cmd_start
from .photo import recive_photo
from .menu import menu_choice
from .blur import blur_choice
from .info import image_info_choice
from .rotate import rotate_choice
from .palette import palette_choice
from .mirror import mirror_choice
from .brightness import brightness_choice
from .thumbnail import (
    thumbnail_choice,
    thumbnail_choice_width,
    thumbnail_choice_height,
    thumbnail_get_result,
)
from .compress import compress_choice
from .watermark import watermark_choice, watermark_receive


def setup(dp: Dispatcher):
    ## Watermark
    dp.register_message_handler(
        watermark_choice,
        state=MainState.WATERMARK,
    )
    dp.register_message_handler(
        watermark_receive,
        state=WatermarkState.UPLOAD,
        content_types=["photo", "document"],
    )
    ##
    ## Compress
    dp.register_message_handler(compress_choice, state=MainState.COMPRESS)
    ## Thumbnail
    dp.register_message_handler(
        thumbnail_choice,
        state=MainState.THUMBNAIL,
    )
    dp.register_message_handler(
        thumbnail_choice_width,
        state=SizeState.WIDTH,
    )
    dp.register_message_handler(
        thumbnail_choice_height,
        state=SizeState.HEIGHT,
    )
    dp.register_message_handler(
        thumbnail_get_result,
        state=SizeState.READY,
    )
    ##

    dp.register_message_handler(
        brightness_choice,
        state=MainState.BRIGHTNESS,
    )
    dp.register_message_handler(
        mirror_choice,
        state=MainState.MIRROR,
    )
    dp.register_message_handler(
        palette_choice,
        state=MainState.PALETTE,
    )
    dp.register_message_handler(
        rotate_choice,
        state=MainState.ROTATE,
    )
    dp.register_message_handler(
        image_info_choice,
        state=MainState.IMAGE_INFO,
    )
    dp.register_message_handler(
        blur_choice,
        state=MainState.BLUR,
    )
    dp.register_message_handler(
        filter_choice,
        state=MainState.FILTERS,
    )
    dp.register_message_handler(
        menu_choice,
        state=MainState.MENU_SHOW,
    )
    dp.register_message_handler(
        recive_photo,
        content_types=["photo", "document"],
        state=MainState.STARTED,
    )
    dp.register_message_handler(cmd_start, CommandStart())
