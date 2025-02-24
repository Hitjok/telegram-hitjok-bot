import os
import gspread
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from oauth2client.service_account import ServiceAccountCredentials
import json

# Настройки бота
TOKEN = os.getenv("TOKEN")
GOOGLE_SHEET_URL = os.getenv("GOOGLE_SHEET_URL")

# Авторизация Google API
credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
credentials_dict = json.loads(credentials_json)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
client = gspread.authorize(creds)
sheet = client.open_by_url(GOOGLE_SHEET_URL)

# Логирование
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Клавиатура с выбором дня недели
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Понедельник"), KeyboardButton("Вторник"), KeyboardButton("Среда"))
keyboard.add(KeyboardButton("Четверг"), KeyboardButton("Пятница"), KeyboardButton("Суббота"), KeyboardButton("Воскресенье"))

# Команда /start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Выбери день недели, чтобы посмотреть задачи:", reply_markup=keyboard)

# Запуск бота
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)