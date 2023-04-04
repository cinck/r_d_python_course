from myfrequentfuncs.myfuncs import intentry

# 1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.


def backward_count(number: int):
    print(number, end=" ")
    if number == 0:
        print()
        return
    backward_count(number - 1)


def fibonacci(number: int):
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)



if __name__ == "__main__":
    some_number = intentry(rangemax=995)
    print(f"Backward count from {some_number}")
    backward_count(some_number)
    for i in range(some_number):
        print(f"Fibonacci n{i} is {fibonacci(i)}")
    print(f"Fibonacci n{some_number} is {fibonacci(some_number)}")

