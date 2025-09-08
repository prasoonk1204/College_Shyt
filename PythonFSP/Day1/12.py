# use of break statement

for i in range(1, 10, 2):
    print("i =", i)
    if (i == 5):
        print("Executing BREAK statement...")
        break
else:
    print("ELSE block is executing...")
print("End of the program...")


# Check whether one user given integer number is PRIME or not
num1 = int(input("Please enter one integer number:"))
for i in range(2, int(num1 ** 0.5) + 1):
    if (num1 % i == 0):
        print(f"{num1} is Not a PRIME number...")
        break
else:
    print(f"{num1} is a PRIME number...")
print("End of the program...")


# use of continue statement
for i in range(1, 11, 1):
    if (i == 3 or i == 5):
        print(f"Executing CONTINUE for i = {i}")
        continue
    print(f"Executing for i = {i}")
else:
    print("ELSE block is executing...")
print("end of the program...")


n = int(input("Please enter the number of numbers:"))
total = 0
for i in range(n):
    num = int(input("Please input an integer number:"))
    if (num < 0): continue
    total = total + num
    print(f"Current number = {num} and total = {total}")
else:
    print("The loop has been terminated...")
print("So the grand total is", total)
print("End of the program...")



num = int(input("Please enter one integer number:"))
if (num >= 0):
    print(f"{num} is a POSITIVE Number")
else:
    pass   # pass is called a statement placeholder
print("End of the program...")



num = int(input("Please enter one integer number:"))
if (num < 0):
    pass
else:
    print(f"{num} is a POSITIVE Number")
print("End of the program...")