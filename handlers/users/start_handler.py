from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer(f'Привет!')
    await message.answer('Вы перешли в режим общения с нейросетью.\n'
                         'Для повышения точности и скорости ответа рекомендуем писать запросы на Английском языке.\n'
                         'Приятного общения!')