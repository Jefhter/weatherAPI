import requests, os
from datetime import datetime
from dotenv import load_dotenv

date = datetime.now() # take the date
load_dotenv() # load the variables at .env
API_KEY = os.getenv("API_KEY") # take API_KEY on .env

def get_weather(city, country_id, API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_id}&APPID={API_KEY}&units=metric"
    response = requests.get(url, params={})
    if response.status_code == 200:
        data = response.json()  
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        print(f"""
            {city}, {country_id.upper()}, {date.strftime("%d/%m/%Y")}
            {date.strftime("%H:%M:%S")}

                Temperature is {temperature}ºC.
                It's feeling {feels_like}ºC.
                Weather Description is "{weather_description}".
                Humidity number is {humidity}%.
        """)
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")

print(get_weather('Brasília', 'br', API_KEY))

