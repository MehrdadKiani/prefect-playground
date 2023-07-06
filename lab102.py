from datetime import timedelta
import httpx
from prefect import flow,task,get_run_logger

@task(retries=2,retry_delay_seconds=15)
def fetch_weather_temperature():
    logger = get_run_logger()
    logger.info("Fetching temperature")
    res = httpx.get("https://httpstat.us/Random/200,500")
    data = res.json()
    logger.info(data["elevation"])

@task()
def calc(number):
    return number * 2

@task()
def print_result(data):
    logger = get_run_logger()
    logger.info(data)

@flow
def main():
    result = calc(4)
    print_result(result)
    temp = fetch_weather_temperature()

    print(temp)

if __name__ == "__main__":
    main()
