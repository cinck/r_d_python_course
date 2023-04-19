from myfrequentfuncs.myfuncs import intentry  # function to obtain integers from input
from time import strftime as s_time, localtime


# <HW12> Task 3
def name_time_deco(times=0):
    """Decorator function can display name and start time of decorated function multiple times
    if 'times' argument is not 0
    :param times: quantity of printed name+time lines
    :return:
    """

    def wrap(some_func):

        def inner_func():
            for i in range(times):
                print(f"{i+1}) Function '{some_func.__name__}' started at {s_time('%H:%M:%S', localtime())}")
            some_func()

        return inner_func

    return wrap


@name_time_deco(times=intentry())
def print_func():
    print("This is the FUNCTION")


if __name__ == "__main__":
    print_func()

