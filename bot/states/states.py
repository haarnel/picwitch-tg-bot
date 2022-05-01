from aiogram.dispatcher.filters.state import State, StatesGroup


class MainState(StatesGroup):
    STARTED = State()
    FILE_UPLOADED = State()
    MENU_SHOW = State()
    FILTERS = State()
    BLUR = State()
    IMAGE_INFO = State()
    ROTATE = State()
    PALETTE = State()
    MIRROR = State()
    BRIGHTNESS = State()
    THUMBNAIL = State()
    COMPRESS = State()
    WATERMARK = State()


class FilterState(StatesGroup):
    LIST = State()


class SizeState(StatesGroup):
    WIDTH = State()
    HEIGHT = State()
    READY = State()


class WatermarkState(StatesGroup):
    UPLOAD = State()
