import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = "8111919704:AAEtOLqEEEEVJGk6jXFEuXQYVdjgMlCeFMA"
ADMIN_ID = 504004158

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Бот работает! Используй /book для бронирования.")

@dp.message_handler(commands=['book'])
async def book(message: types.Message):
    await message.reply("Ты сделал бронирование!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
