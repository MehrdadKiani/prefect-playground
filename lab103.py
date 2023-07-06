from prefect import flow, task, get_run_logger

@task()
def who_is(user: str):
    logger = get_run_logger()
    logger.info("This task called by {}!".format(user))


@flow
def main(default:str ='unknown'):
    who_is(default)


if __name__ == "__main__":
    main(default='Kiani')
