from aiogram import Dispatcher
from .privat_chat import IsPrivate
from .Admin_Filter import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsAdmin)