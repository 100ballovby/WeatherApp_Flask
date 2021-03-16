import requests
from flask import request
from app import app
import os  # работа с операционной системой (компьютера\сервера)


@app.route('/city')
def search_weather():
    API_KEY = os.environ.get('API_KEY')  # ваш ключ будет храниться туть
    city = request.args.get('q')

    # make a call
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url).json()
    # 200, 300, 400, 500
    if response.get('cod') != 200:
        # если подключение не успешно
        message = response.get('message', '')
        return f'Error getting data for {city.title()}, Error message - {message}'

    current_temp = response.get('main', {}).get('temp')
    if current_temp:
        celsium = current_temp - 273.15
        return f'Current temperature of {city.title()} is {celsium}.'
    else:
        return f'Error getting temperature for {city.title()}.'

# http://127.0.0.1:5000/city?q=minsk
