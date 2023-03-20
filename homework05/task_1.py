# ========= The character analyzing program =========
# This program analyzes and describes every character
# of the user's keyboard entry.
#  ! To finish program from running type 'exit' !
# ===================================================

user_input = ""
while user_input.lower() != "exit":
    print("------------------------------------------------")

    user_input = input("Please enter your data or type 'exit' to finish: -> ")

    if not user_input or user_input.lower() == "exit":
        continue

    print("------------------------------------------------")

    for char in user_input:

        if char.isdigit():
            odd_or_even = "odd"
            if int(char) % 2 == 0:
                odd_or_even = "even"
            print(f"'{char}' is an {odd_or_even} number.")

        elif char.isalpha():
            upper_or_lower = "an upper"
            if char.islower():
                upper_or_lower = "a lower"
            print(f"'{char}' is {upper_or_lower} case letter.")

        elif char.isspace():
            print(f"'{char}' is a space.")

        else:
            print(f"'{char}' is a symbol.")
