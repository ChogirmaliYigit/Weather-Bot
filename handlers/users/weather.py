import requests
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS, API_key
from loader import dp, db, bot
from api import with_lat_lon, with_city_name
from states.weather import WeatherState

@dp.message_handler(text="📍 Lokatsiya jo'natish", state=WeatherState.get_city_or_location)
async def send_weather(message: types.Message):
    response = with_lat_lon(API_key=API_key, lat=message.location.latitude, lon=message.location.longitude)
    print(response)

@dp.message_handler(state=WeatherState.get_city_or_location)
async def send_weather(message: types.Message):
    response = with_city_name(API_key=API_key, city_name=message.text)
    print(response)
