from filters import IsAdmin
from loader import dp
from aiogram.types import Message
from states import ChatGpt


@dp.message_handler(IsAdmin(), commands=['start'])
async def start(message: Message):
    await message.answer(f'Привет!')
    await message.answer('Вы перешли в режим общения с нейросетью.\n'
                         'Для повышения точности и скорости ответа рекомендуем писать запросы на Английском языке.\n'
                         'Приятного общения!')
    await ChatGpt.gpt.set()

