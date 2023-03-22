from task_02 import enter_elements

# <HW> Task3: Find the highest element of an array
# <HW> - create own function
def find_max(array):
    max_ = array[0]
    # <HW> - use lambda function
    compare = lambda m, i: m if (m > i) else i

    for pos in range(1, len(array)):
        intermediate = compare(array[pos], max_)
        max_ = intermediate

    return max_


def main():
    elements = enter_elements("numbers")
    print("==================")
    print(f"Maximum value from {elements} by ")
    print("Built in function: ", max(elements))  # <HW> - use built in function
    print("Custom function:   ", find_max(elements))


if __name__ == "__main__":
    main()