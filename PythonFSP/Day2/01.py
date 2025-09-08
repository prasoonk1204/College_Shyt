i = 1
while(i <= 10):
    print(f"Looping for i = {i}...")
    i += 1
else:
    print("Executing ELSE block...")
print("End of the program...")


# Check whether one user given integer number is PRIME or not
num1 = int(input("Please enter one integer number:"))
factor = 2
while (factor <= int(num1 ** 0.5)):
    if (num1 % factor == 0):
        print(f"{num1} is Not a PRIME number...")
        break
    factor += 1
else:
    print(f"{num1} is a PRIME number...")
print("End of the program...")



print("Visit doctor...")  # 1 time
for day in range(1, 6):
    print("Good Morning...")  # 5 times
    for medi in range(1, 4):
        print(f"Day No. - {day} and Medicine No. - {medi}...")  # 15 times
    print("Good Night...")  # 5 times
    print("----------------------------------------------")  # 5 times
print("Thanks to Doctor...")  # 1 time
print("End of the story...")  # 1 time


# Classwork: Write the previos example with nested while loops.
print("Visit doctor...")  # 1 time
day = 1
medicount = 0
while (day <= 5):
    print("Good Morning...")  # 5 times
    medi = 1
    while(medi <= 3):
        print(f"Day No. - {day} and Medicine No. - {medi}...")  # 15 times
        medi += 1
        medicount += 1
    print("Good Night...")  # 5 times
    print("----------------------------------------------")  # 5 times
    day += 1
print("Thanks to Doctor...")  # 1 time
print(f"Total number of medicine consumed is {medicount}...")
print("End of the story...")  # 1 time
