from myfrequentfuncs.myfuncs import intentry  # function to accept only integers from input()


# <HW10> Task_1. Recursive function that prints countdown from entered number
def backward_count(number: int):
    """
    Prints reversed count from number
    :param number: any integer
    :return: None
    """
    print(number, end=" ")
    if number == 0:
        print()
        return
    backward_count(number - 1)


# <HW10> Task_2*. Recursive function to get fibonacci numbers
def fibonacci(number: int):
    """
    Returns value of n element in Fibonacci sequence
    :param number: int, sequence number of element
    :return: int
    """
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


# <WH10> Task_3*. Recursive function to calculate factorial
def factorial(number: int):
    """
    Returns calculated value of argument in factorial
    :param number: int
    :return: int
    """
    if number <= 0:
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    some_number = intentry(rangemax=995)
    print("-------------------------")
    print(f"Backward count from {some_number}")
    backward_count(some_number)
    print("-------------------------")
    print(f"Fibonacci n{some_number} is {fibonacci(some_number)}")
    print("-------------------------")
    print(f"Factorial calculation: {some_number}! = {factorial(some_number)}")
