import requests

# 1. За допомогою https://open-meteo.com/ дістати прогноз погоди для 5ти ваших улюблених міст на планеті.
#    Реалізувати за допомогою модуля requests з використанням мультипотоковості і мультипроцесорності.
#
# 2. Знайти середню температуру по прогнозу для кожного міста і вивести в якому місті зараз найспекотніше.
#
# 3. Вивести різницю по часу виконання програми використовуючи потоки і процеси.


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
    else:
        print("'lat' and/or 'long' args are missing")






locations = {
    "Kyiv": {"lat": 50.45, "long": 30.52},
    "Lviv": {"lat": 50.45, "long": 30.52},
    "Bangkok": {"lat": 13.75, "long": 100.50},
    "London": {"lat": 51.51, "long": -0.13},
    "Sydney": {"lat": -33.87, "long": 151.21},
}

get_temp(**locations['Kyiv'], f_d=1)
