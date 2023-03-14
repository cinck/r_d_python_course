print("Lets go!")
# Program that reads input data from user and determines whether it is whole number, single word or none of them.
# It counts letters in word, checks if number is even or odd.

input_data = input("Please type something here: -> ")

if input_data.isalpha():
    if len(input_data) != 1:
        print(f"It is a word '{input_data}' which consists of {len(input_data)} letters.")
    else:
        print(f"It is only single letter '{input_data}'.")

elif input_data.isdigit():
    if (int(input_data) % 2) == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    print(f"'{input_data}' is a whole {odd_even} number.")

else:
    text = "There's no any data."
    if len(input_data) == 1:
        text = f"'{input_data}' is a single symbol or space."
    elif len(input_data) > 1:
        text = f"'{input_data}' consists of multiple types of characters and/or includes symbols and spaces."
    print(text)
