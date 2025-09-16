import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твой токен и Telegram ID можно оставить здесь для теста, но лучше через Render Environment Variables
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8111919704:AAEtOLqEEEEVJGk6jXFEuXQYVdjgMlCeFMA")
ADMIN_ID = int(os.environ.get("ADMIN_ID", "504004158"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Бот работает! Используй команду /book YYYY-MM-DD для бронирования.")

@dp.message_handler(commands=['book'])
async def book_event(message: types.Message):
    await message.reply("Бронирование принято!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
