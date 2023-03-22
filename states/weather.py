from aiogram.dispatcher.filters.state import StatesGroup, State

class WeatherState(StatesGroup):
    get_city_or_location = State()
