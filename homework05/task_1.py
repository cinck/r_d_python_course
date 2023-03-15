# This program analyzes every character of the user's keyboard entry.
# To finish program from running type 'exit'

user_input = ""
while user_input.lower() != "exit":
    print("----------------------------------------")

    for char in user_input:
        if char.isdigit():
            odd_or_even = "odd"
            if int(char) % 2 == 0:
                odd_or_even = "even"
            print(f"'{char}' is {odd_or_even} number")
        elif char.isalpha():
            case = "upper case"
            if char.islower():
                case = "lower case"
            print(f"'{char}' is {case} letter")
        elif char.isspace():
            print(f"'{char}' is a space")
        else:
            print(f"'{char}' is a symbol")

    print("----------------------------------------")
    user_input = input("Please enter your data or type 'exit' to finish: -> ")
