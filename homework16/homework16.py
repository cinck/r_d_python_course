import requests
import time
import threading as thr

# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
#    Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
#
# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
#
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.


class City:

    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.coordinates = {"latitude": latitude, "longitude": longitude}
        self.latitude = latitude
        self.longitude = longitude
        self.temp_forcast = None
        self.average_temp = None
        self.forcast_days = None
#        self.get_temp_forcast(1)

    def get_temp_forcast(self, days: int, attempt=0):
        try:
            resp = requests.get(
                url="https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": self.latitude,
                    "longitude": self.longitude,
                    "forecast_days": days,
                    "hourly": "temperature_2m",
                }
            )
            self.temp_forcast = resp.json()["hourly"]["temperature_2m"]
            self.forcast_days = days

        except Exception as ex:
            print(ex)
            if attempt < 5:
                self.get_temp_forcast(days, attempt+1)
            else:
                print(f"Exceeded {attempt} attempts")
        finally:
            self.set_avg_temp()

    def set_avg_temp(self):
        if self.temp_forcast:
            self.average_temp = sum(self.temp_forcast)/len(self.temp_forcast)


def execute_in_threading(locations: dict):
    cities = {}
    threads = []
    thr_no = 0
    for city, coordinates in locations.items():
        cities[city] = City(city, *coordinates)
        threads.append(thr.Thread(target=cities[city].get_temp_forcast, args=(2, )))
        threads[thr_no].start()
        print(f"Cycle: {thr_no}\nActive threads: {thr.active_count()}")
        thr_no += 1

    for thread in threads:
        thread.join()

    return cities


def get_hottest_city(cities: dict):
    max_temp_city = None
    for city in cities.values():
        print(f"{city.name} temp= {city.average_temp}C")
        if not max_temp_city:
            max_temp_city = city
        elif city.average_temp > max_temp_city.average_temp:
            max_temp_city = city

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

    cities = execute_in_threading(locations)

    hottest_city = get_hottest_city(cities)

    print(f"Hottest city is {hottest_city.name} with average temperature {hottest_city.average_temp}")

    print(time.time()-t_start)
