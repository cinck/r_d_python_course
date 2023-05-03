import requests
import time
import threading as thr
import multiprocessing as mp

# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
#    Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
#
# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
#
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.


class City:

    def __init__(self, name: str, latitude: float, longitude: float, days=1):
        self.name = name
        self.coordinates = {"latitude": latitude, "longitude": longitude}
        self.latitude = latitude
        self.longitude = longitude
        self.temp_forecast = None
        self.average_temp = None
        self.forecast_days = days
#        self.get_temp_forcast(1)

    def get_temp_forcast(self, days=1, attempt=0):
        try:
            resp = requests.get(
                url="https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                    "forecast_days": self.forecast_days,
                    "hourly": "temperature_2m",
                }
            )
            self.temp_forecast = resp.json()["hourly"]["temperature_2m"]

        except Exception as ex:
            print(ex)
            if attempt < 5:
                self.get_temp_forcast(days, attempt+1)
            else:
                print(f"Exceeded {attempt} attempts")
        finally:
            self.set_avg_temp()

    def set_avg_temp(self):
        if self.temp_forecast:
            self.average_temp = round(sum(self.temp_forecast) / len(self.temp_forecast), 2)


def get_forecast(city):
    city.get_temp_forcast()
    return city


def execute_in_processes(locations: dict):
    mp_start = time.time()
    cities2 = []

    for city_name, coordinates in locations.items():
        cities2.append(City(city_name, *coordinates))

    with mp.Pool(5) as pool:
        forecasted = pool.map(get_forecast, cities2)

    print(f"Multiprocessing time: {time.time() - mp_start}")

    return forecasted


def execute_in_threading(locations: dict):
    mt_start = time.time()
    cities = []
    threads = []
    counter = 0
    for city, coordinates in locations.items():
        cities.append(City(city, *coordinates))
        threads.append(thr.Thread(target=cities[counter].get_temp_forcast, args=(1, )))
        threads[counter].start()
        # print(f"Cycle: {counter}\nActive threads: {thr.active_count()}")
        counter += 1

    for thread in threads:
        thread.join()

    print(f"Threading time: {time.time() - mt_start}")

    return cities


def get_hottest_city(cities: list):
    max_temp_city = None

    for city in cities:
        if not max_temp_city:
            max_temp_city = city
        elif city.average_temp > max_temp_city.average_temp:
            max_temp_city = city

    print(f"Hottest city is {max_temp_city.name} with average temperature {max_temp_city.average_temp} C")

    return max_temp_city


if __name__ == "__main__":
    t_start = time.time()

    locations = {
        "Kyiv": (50.45, 30.52),
        "Lviv": (50.45, 30.52),
        "Bangkok": (13.75, 100.50),
        "London": (51.51, -0.13),
        "Sydney": (-33.87, 151.21),
    }

    mt_cities = execute_in_threading(locations)

    mp_cities = execute_in_processes(locations)

    get_hottest_city(mt_cities)
    get_hottest_city(mp_cities)

    print(f"Full time {time.time()-t_start}")
