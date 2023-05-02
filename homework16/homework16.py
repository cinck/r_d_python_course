import requests
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
        finally:
            self.set_avg_temp()

    def set_avg_temp(self):
        if self.temp_forcast:
            self.average_temp = sum(self.temp_forcast)/len(self.temp_forcast)




def get_temp(*args, **kwargs):
    print(args)
    print(kwargs)
    parameters = {
        "lat": 0,
        "long": 0,
        "f_d": 1
    }
    for parameter, value in kwargs.items():
        parameters[parameter] = value

    if parameters['lat'] and parameters['long'] and parameters["f_d"] in range(1,10):
        lat = parameters['lat']
        long = parameters['long']
        print(lat, long)

        resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": long,
                "forecast_days": 1,
                "hourly": "temperature_2m",
            }
        )

        print(resp)
        temperature_list = resp.json()["hourly"]["temperature_2m"]
        print(temperature_list)
        for i in temperature_list:
            print(i)

        return temperature_list

    else:
        print("'lat' and/or 'long' args are missing")


def average(temp, tr_no):
    for i in temp:
        i **= i
        # print(f"thr_no {tr_no}")
    return sum(temp)/len(temp)


def compare_weather(locations: dict):
    print(thr.active_count())
    threads = []
    thr_no = 0
    for city, coordinatesin in locations.items():
        threads.append(thr.Thread(target=average, args=([24592+thr_no, 10], thr_no )))
        threads[thr_no].start()
        print(f"Cycle: {thr_no}\nActive threads: {thr.active_count()}")
        thr_no += 1
        print(threads)


    for thread in threads:
        thread.join()

    print(thr.active_count())
    pass


locations = {
    "Kyiv": {"coordinates": {"lat": 50.45, "long": 30.52}},
    "Lviv": {"coordinates": {"lat": 50.45, "long": 30.52}},
    "Bangkok": {"coordinates": {"lat": 13.75, "long": 100.50}},
    "London": {"coordinates": {"lat": 51.51, "long": -0.13}},
    "Sydney": {"coordinates": {"lat": -33.87, "long": 151.21}},
}

# get_temp(**locations, f_d=1)
compare_weather(locations)
