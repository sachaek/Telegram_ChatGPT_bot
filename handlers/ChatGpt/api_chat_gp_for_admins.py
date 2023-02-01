import html
import os
import openai
from aiogram.types import Message
from filters import IsAdmin
from loader import dp, bot
from dotenv import load_dotenv

load_dotenv()


def gpt(prompt):
    openai.api_key = os.getenv("API_GPT")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(prompt),
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
        )
    answer = html.escape(str(response['choices'][0]['text']))
    return answer


@dp.message_handler(IsAdmin())
async def chatting(message: Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"""{gpt(message.text)}""",
                           parse_mode="HTML")

