# ========= The character analyzing program =========
# This program analyzes and describes every character
# of the user's keyboard entry.
#  ! To finish program from running type 'exit' !
# ===================================================

user_input = ""
while user_input.lower() != "exit":
    print("----------------------------------------")

    for char in user_input:
        char_type = ""
        char_property = ""

        if char.isdigit():
            char_type = "number"
            char_property = "an odd"
            if int(char) % 2 == 0:
                char_property = "an even"

        elif char.isalpha():
            char_type = "letter"
            char_property = "an upper case"
            if char.islower():
                char_property = "a lower case"

        elif char.isspace():
            char_type = "space"
            char_property = "a"

        else:
            char_type = "symbol"
            char_property = "a"

        print(f"'{char}' is {char_property} {char_type}")

    print("----------------------------------------")
    user_input = input("Please enter your data or type 'exit' to finish: -> ")
