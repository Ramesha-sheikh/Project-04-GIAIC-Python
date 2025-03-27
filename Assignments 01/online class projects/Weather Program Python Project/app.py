# Project: Weather Program
# Yeh program kisi bhi shehar ka mausam check karne ke liye hai.
# Yeh OpenWeather API ka use karega.

# Required Library:
# is project ke liye aapko `requests` install karni hogi.
# Install karne ke liye terminal me yeh command chalayein:
# pip install requests

import requests

def get_weather(city):
    """Diye gaye shehar ka mausam ka data retrieve karega."""
    API_KEY = "YOUR_API_KEY"  # Yahan apni OpenWeather API key dalein
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Shehar: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Shehar ka data nahi mila, dubara check karein!")

if __name__ == "__main__":
    city = input("Shehar ka naam enter karein: ")
    get_weather(city)
