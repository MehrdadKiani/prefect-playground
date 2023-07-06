import httpx
from prefect import flow,task

@task
def fetch_weather_temperature():
    res = httpx.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
    return res.json()

@task
def fetch_weather_windspeed():
    res = httpx.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=windspeed_10m")
    return res.json()

@task
def fetch_weather_weathercode():
    res = httpx.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
    return res.json()

@flow
def main():
    temp = fetch_weather_temperature()
    wind = fetch_weather_windspeed()
    weat = fetch_weather_weathercode()

    print(temp)
    print(wind)
    print(weat)

if __name__ == "__main__":
    main()
