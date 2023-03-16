# ======= TASK 4 ======
# Program that reads input data from user and determines whether it is whole number, single word or none of them.
# It counts letters in word, checks if number is even or odd.

# Cheering up
print("Lets go!")

# ===== TASK 01 ========
# Waiting for data entry
user_input = input("Please type something here: -> ")

# Task3: If user's entry is a word, counts number of letters.
if user_input.isalpha():
    if len(user_input) != 1:
        print(f"It is a word '{user_input}' which consists of {len(user_input)} letters.")
    else:
        print(f"It is only single letter '{user_input}'.")

# Task 2: If user's entry is a number, determines it's odd or even.
elif user_input.isdigit():
    if int(user_input) % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"'{user_input}' is a whole {odd_or_even} number.")

else:
    match len(user_input):
        case 0:
            print("There's no any data.")
        case 1:
            space_or_symbol = "symbol"
            if user_input == " ":
                space_or_symbol = "space"
            print(f"'{user_input}' is a {space_or_symbol}.")
        case _:
            print(f"'{user_input}' consists of multiple types of characters and/or includes symbols and spaces.")
