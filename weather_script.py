import requests

def get_weather(city):
    api_key = "6c4f3ab5c7331af19627d575b85ffead"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        print(f"Weather in {city}: {temperature}°C, {weather_desc}")
    else:
        print("Failed to fetch weather data.")

# Example usage
city = "London"
get_weather(city)