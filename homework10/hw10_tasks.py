from myfrequentfuncs.myfuncs import intentry

# 1. Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.


def backward_count(number):
    print(number, end=" ")
    if number == 0:
        print()
        return None
    return backward_count(number - 1)


if __name__ == "__main__":
    some_number = intentry(rangemax=995)
    backward_count(some_number)


