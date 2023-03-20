from time import sleep

# ===== THE INFINITE LOOP PROGRAM =====
# Prints 'I love Python!' every 4.2 sec
# =====================================

# Start warning
print("-====== !! WARNING !! ======-")
sleep(2)
print("The infinite loop start is in ..")

# Countdown
for i in ["FIVE", "FOUR", "THREE", "TWO", "ONE"]:
    sleep(1.25)
    print(f". {i} !")

sleep(1)
print("=======< Launch! >=======")

# THE LOOP!
while True:
    sleep(4.2)
    print("I love Python!")
