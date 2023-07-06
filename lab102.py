from datetime import timedelta
import httpx
from prefect import flow, task, get_run_logger
import pandas as pd


@task(retries=2, retry_delay_seconds=15)
def fetch_weather_temperature():
    logger = get_run_logger()
    logger.info("Fetching temperature")
    res = httpx.get("https://httpstat.us/Random/200,500")
    data = res.json()
    logger.info(data["elevation"])


@task
def calc(number):
    # create a dictionary to store the result
    dict_data = {'result': number * 2}
    return dict_data


@task
def print_result(data):
    logger = get_run_logger()
    logger.info(data)


@task()
def store_df():
    df = pd.DataFrame([['Ajitesh', 84, 183, 'no'],
                       ['Shailesh', 79, 186, 'yes'],
                       ['Seema', 67, 158, 'yes'],
                       ['Nidhi', 52, 155, 'no']])
    return df


@flow
def main():
    result = calc(4)
    print_result(result)
    store_df()
    # print(fetch_weather_temperature())


if __name__ == "__main__":
    main()
