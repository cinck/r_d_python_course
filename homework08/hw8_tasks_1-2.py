# 1. Написати функцію, яка повертає тільки однакові елементи двох множин.
#
# 2. Написати функцію, яка повертає тільки унікальні елементи двох множин.


def same_items(set1: set, set2: set):
    """
    <HW Task 1> Function that returns same elements from two sets
    :param set1: set()
    :param set2: set()
    :return: set()
    """
    return set1.intersection(set2)


def unique_items(set1: set, set2: set):
    """
    <HW Task 2> Function that returns only unique elements from two sets
    :param set1: set()
    :param set2: set()
    :return: set()
    """
    return set1.symmetric_difference(set2)


if __name__ == "__main__":
    set1 = set(range(15))
    set2 = set(range(5, 20))
    print(f"Set1: {set1}")
    print(f"Set2: {set2}")
    print(f"Same items in set1 and set2: {same_items(set1, set2)}")
    print(f"Unique items in set1 and set2: {unique_items(set1, set2)}")
