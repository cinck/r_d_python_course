# <HW31> Task 2: Show weather in requested city.

import requests


def get_city_data(city_name: str):
    try:
        result = requests.get(
            url="https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city_name,
                "count": 1
            }
        )
    except Exception:
        print("Failed to get")
        return None
    try:
        data = result.json()["results"]
    except Exception:
        print(f"No such city <{city_name}> found. Check spelling and try again.")
        return None
    return data


def decode_wthr_condition(code):
    if code in range(10):
        return "good"
    elif code in range(41, 50):
        return "foggy"
    elif code in range(51, 60):
        return "drizzly"
    elif code in range(61, 70):
        return "rainy"
    elif code in range(71, 80):
        return "snowy"
    elif code in range(80, 100):
        return "trying to kill you!"
    else:
        return "unknown"


def get_weather_in(city_name: str):
    city_data = get_city_data(city_name)
    print(city_data)
    if not city_data:
        return None
    try:
        resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": city_data[0]["latitude"],
                "longitude": city_data[0]["longitude"],
                "current_weather": True
            }
        )
    except Exception:
        print("Can't receive weather. Try again later.")
        return None
    finally:
        pass
    print(resp.json())
    temp = resp.json()["current_weather"]["temperature"]
    weather_code = resp.json()["current_weather"]["weathercode"]
    condition = decode_wthr_condition(weather_code)
    print(f"Current weather in {city_name} is {condition}. Temperature: {temp} degrees.")
    return temp, condition


if __name__ == "__main__":
    city = input("Enter city name: > ").capitalize()
    get_weather_in(city)