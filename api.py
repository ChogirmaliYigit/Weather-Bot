import requests

def with_lat_lon(API_key, lat, lon):
    link = f'https://api.weatherapi.com/v1/current.json?key={API_key}&q={lat},{lon}'
    response = requests.get(link).json()
    return response

def with_city_name(API_key, city_name):
    link = f'https://api.weatherapi.com/v1/current.json?key={API_key}&q={city_name}'
    response = requests.get(link).json()
    return response
