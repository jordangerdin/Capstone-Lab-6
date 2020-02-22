import requests
import datetime
import os
from dotenv import load_dotenv
from pathlib import Path
from pprint import pprint

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

host = 'https://api.openweathermap.org/'
path = 'data/2.5/forecast'
key = os.getenv('WEATHER_KEY')

city = input('Enter a city: ')

query = '?q=' + city + '&units=imperial'

url = host + path + query + '&appid=' + key
data = requests.get(url).json()

forecast_items = data['list']

for forecast in forecast_items:
    date = forecast['dt']
    time = datetime.datetime.fromtimestamp(date).ctime()
    temp = forecast['main']['temp']
    desc = forecast['weather'][0]['description']
    windspeed = forecast['wind']['speed']

    print('On ' + time + ' the weather will be ' + str(temp) + ' F, \n\t' + str(desc) + ' and a wind speed of ' + str(windspeed) + ' mph.')