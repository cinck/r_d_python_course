def rise_to_power(number, power):
    return number ** power


def users_entry(entry_request: str):
    number_input = input(f"Enter {entry_request}: -> ")
    if number_input and number_input.isdigit():
        return int(number_input)
    else:
        print("You should enter only whole numbers. Try again.")
        return users_entry(entry_request)


def run():
    number = users_entry("your number")
    power = users_entry("power value")
    print("---------RESULT---------")
    print(f"{number}^{power} = {rise_to_power(number, power)}")
    print("------------------------")
    if input("Type 'R' to retry or anything else to finish: -> ").lower() == "r":
        run()


if __name__ == "__main__":
    run()
