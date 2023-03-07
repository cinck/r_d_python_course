
# 1. Використовуючи функцію print, надрукувати фразу “I love Python” 42 рази.
print("Task 1:")
print("I love Python\n" * 42)

# 2. Створити змінну age_in_month, надавши їй значення вашого поточного віку в місяцях.
print("\nTask 2:")
age_in_month = 451
print(age_in_month)

# 3. Створити змінну age_in_years, в яку записати ваш вік в роках на основі попередньої змінної.
print("\nTask 3:")
age_in_years = age_in_month//12
print(age_in_years)

# 4. Створити змінну my_age, яка буде містити рядок “Му name is … I’m … years old”,
#   де на замість пропусків буде підставлятись ваші імʼя та вік.
#   Значення віку слід брати зі змінної age_in_years.
print("\nTask 4:")
name = "Oleksandr"

my_age = f"My name is {name}. I'm {age_in_years} years old."

print(my_age)

# 5. Створити змінну зі значенням 1. Використовуючи оператори порівняння,
#   порівняти її із будь-якими іншими значеннями (мінімум 5 порівнянь)
#   і перевірити вивід в інтерпретаторі.
print("\nTask 5:")
new_var = 1
print(f"Is my number == \'1\' ?  -{new_var == '1'}")
print(f"Is my number > 2 ?  -{new_var > 2}")
print(f"Is my number < 5 ?  -{new_var < 5}")
print(f"Is my number != 1 ?  -{new_var != 1}")
print(f"Is my number == 1 ?  -{new_var == 1}")

# 6. Створити змінні a=2, b=5, c=6. На основі цих змінних створити змінну d,
#   значення якої має бути “256”
print("\nTask 6:")
a, b, c = 2, 5, 6
d = int(str(a) + str(b) + str(c))
print(f"d = {d}")
