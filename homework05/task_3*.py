# ===== The triangle pattern =====

number_of_lines = ""
while number_of_lines not in range(1, 10):
    number_of_lines = input("Please type any number between 1 and 9: ")
    if number_of_lines.isdigit():
        number_of_lines = int(number_of_lines)

for i in range(1, int(number_of_lines)+1):
    text = ""
    for k in range(1, i+1):
        text = text + str(k)
    print(text)

