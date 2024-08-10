import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import TOKEN, WEATHER_API

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Сегодня я бот, который присылает погоду!")

@dp.message(Command(commands='help'))
async def help(message: Message):
    await message.answer("Чтобы получить погоду в Москве введите команду /weather")

@dp.message(Command(commands='weather'))
async def get_weather(message: Message):
     data = get_weather('Moscow')
     text = f"Сейчас в Москве {data['main']['temp']}°C, {data['weather'][0]['description']}"
     await message.answer(text)

def get_weather(city):
    api_key = WEATHER_API
    print(api_key)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={api_key}"
    print(url)
    response = requests.get(url)
    print(response.json())
    return response.json()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())