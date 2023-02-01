from aiogram.dispatcher.filters.state import StatesGroup, State


class ChatGpt(StatesGroup):
    gpt = State()
    customization = State()
    temperature = State()
    responses = State()

