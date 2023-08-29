import pytest


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


def test_fibonacci_success():
    fibs = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21
    }
    for n, f in fibs.items():
        assert fibonacci(n) == fibs[n]


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        assert fibonacci('1')
        assert fibonacci([2])
        assert fibonacci(None)
        assert fibonacci({2: 1, 3: 2,})
