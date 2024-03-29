# 3. (необов'язкове виконання) Перетворити всі елементи списку типу string
#    в верхній регістр, використовуючи map.
#
# 4. (необов'язкове виконання) Вивести всі елементу масиву,
#    які є числом, використовуючи filter.

def strings_to_upper(item):
    """
    Returns string argument converted to upper case
    :param item:
    :return:
    """
    if isinstance(item, str):
        return item.upper()
    return item


def only_numeric(item):
    """
    Returns back argument if it is a numeric item.
    :param item:
    :return:
    """
    return isinstance(item, (int, float))


if __name__ == "__main__":
    # making list of multiple types items
    some_list = [1, 3.5, True, "oxygen", (1, "great 18"), 0, False, "9 rings of hell", -0.24]
    print(f"Some list:\n{some_list}")
    print()
    # <HW Task 3> Mapping all str items to upper case
    mapped_list = tuple(map(strings_to_upper, some_list))
    print(f"Modified list:\n{mapped_list}")
    print()
    # <HW Task 4> Filtering numeric items
    filtered_list = tuple(filter(only_numeric, some_list))
    print(f"Numbers found in all items of the list:\n{filtered_list}")
