from time import strftime as s_time, sleep


# <HW12> Task1
def func_name_time(some_func):
    """Decorator function displays name of function which is decorated and start time of function operation"""

    def inner_func(*args, **kwargs):
        print(f"Function '{some_func.__name__}' started at {s_time('%H:%M:%S')}")
        return some_func(*args, **kwargs)

    return inner_func


@func_name_time
def my_function():
    print("This is my function")
    return 10


@func_name_time
def my_function2():
    print("My second function")


if __name__ == "__main__":
    print(my_function())
    sleep(3)
    my_function2()
