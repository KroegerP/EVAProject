import os
from functools import wraps
import time


def on_rpi():
    return os.getenv("APP_ENV") in ["staging", "production"]


def env_wrapper(func):
    """
    Wrapped function will only run if `$APP_ENV` is `staging` or `production`.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        app_env = os.getenv("APP_ENV")
        if app_env == "development":
            print("App in development mode, not performing action!")
            return
        elif app_env == "staging" or app_env == "production":
            return func(*args, **kwargs)
        else:
            raise ValueError(f"Invalid APP_ENV: {app_env}")

    return inner


def time_wrapper(func):
    """
    Add this decorator to time how long it takes to execute a function.
    """

    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()

        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute")

        return result

    return inner
