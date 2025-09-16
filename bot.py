from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Bot is running! Use /book YYYY-MM-DD to book.")

@dp.message_handler(commands=['book'])
async def book_event(message: types.Message):
    await message.reply("Booking received!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
