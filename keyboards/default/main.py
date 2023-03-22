from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


weather_markup = ReplyKeyboardMarkup(resize_keyboard=True)
weather_markup.insert(KeyboardButton(text="📍 Lokatsiya jo'natish", request_location=True))
