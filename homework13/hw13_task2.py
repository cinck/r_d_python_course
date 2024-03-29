import os
from time import strftime


def log_name_time(some_func):
    """Decorator function saves name of function and time when it's called into log file"""

    def inner_func(*args, **kwargs):
        if not os.path.exists("logs"):
            os.mkdir("logs")
        with open(f"logs/{__name__}_log.txt", "a") as log_file:
            log_file.write(
                f"{strftime('%Y-%m-%d %H:%M:%S')} started function '{some_func.__name__}'\n")

        return some_func(*args, **kwargs)

    return inner_func
