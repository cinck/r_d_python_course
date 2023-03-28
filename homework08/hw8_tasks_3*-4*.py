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
    if isinstance(item, (str,)):
        return item.upper()
    return item


def only_numeric(item):
    """
    Returns back argument if it is a numeric item.
    :param item:
    :return:
    """
    if isinstance(item, (int, float)) and not isinstance(item, (bool,)):
        return item


if __name__ == "__main__":
    some_list = [1, 3.5, True, "oxygen", (1, "great 18"), 0, False, "9 rings of hell", -0.24]
    print(f"Some list:\n{some_list}")
    print()

    mapped_list = tuple(map(strings_to_upper, some_list))
    print(f"Modified list:\n{mapped_list}")
    print()

    filtered_list = tuple(filter(only_numeric, some_list))  # 0 (zero) is always filtered away
    print(f"Numbers found in all items of the list:\n{filtered_list}")
