import requests
import datetime
import os
from pprint import pprint

host = 'https://api.openweathermap.org/'
path = 'data/2.5/forecast'
key = os.environ.get('WEATHER_KEY')

city = input('Enter a city: ')

query = '?q=' + city + '&units=imperial'

url = host + path + query + '&appid=' + key
data = requests.get(url).json()

forecast_items = data['list']

for forecast in forecast_items:
    date = forecast['dt']
    readable = datetime.datetime.fromtimestamp(date).ctime()
    temp = forecast['main']['temp']
    desc = forecast['main']['']

    print('At ' + readable + ' temp will be ' + str(temp) + ' F')