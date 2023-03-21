# Program that raises numbers to power
# User can entry number and power values for calculation.
# Note only natural numbers are accepted for both numbers and powers.

# HW.Task 1: Function that raises number to power from two arguments.
def raise_to_power(number, power):
    return number ** power


# Accepts user's input, checks it and returns integer if entry data is correct.
def users_entry(entry_request: str) -> int:
    number_input = input(f"Enter {entry_request}: -> ")
    if number_input and number_input.isdigit():
        return int(number_input)
    else:
        print("You should enter only whole numbers. Try again.")
        return users_entry(entry_request)


# Main function
def run():
    print(" -= RAISING TO POWER =-")
    number = users_entry("your number")
    power = users_entry("power value")
    print("---------RESULT---------")
    print(f"{number}^{power} = {raise_to_power(number, power)}")
    print("------------------------")
    if input("Type 'R' to restart or anything else to finish: -> ").lower() == "r":
        print("------------------------")
        run()


if __name__ == "__main__":
    run()
