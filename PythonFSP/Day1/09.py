# Conditional Statements

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if (num1 >= num2):
    if (num1 >= num3):
        print(num1, " is the largest number")
    else:
        print(num3, " is the largest number")
else:
    if (num2 >= num3):
        print(num2, " is the largest number")
    else:
        print(num3, " is the largest number")



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# 2nd largest number
if (num1 >= num2) and (num1 >= num3):
    if (num2 >= num3):
        print(num2, "is the 2nd largest number")
    else:
        print(num3, "is the 2nd largest number")
elif (num2 >= num1) and (num2 >= num3):
    if (num1 >= num3):
        print(num1, "is the 2nd largest number")
    else:
        print(num3, "is the 2nd largest number")
else:
    if (num1 >= num2):
        print(num1, "is the 2nd largest number")
    else:
        print(num2, "is the 2nd largest number")


if (num1 >= num2 and num1 >= num3):
        print("The FIRST number is the maximum number....")
        print("So the maximum number is", num1)
elif (num2 >= num3):
    print("The SECOND number is the maximum number....")
    print("So the maximum number is", num2)
else:
    print("The THIRD number is the maximum number....")
    print("So the maximum number is", num3)
print("End of the program...")

# LOGIC
# input num1, num2, num3
# if (num1 < num2) then swap num1, num2
#               num1             num2
#               700              400
# num3 =>  800                             num1 = 700
# num3 =>                500               num3 = 500
# num3 =>                             100  num2 = 400

if (num1 < num2): num1, num2 = num2, num1
if (num3 >= num1): print("Second Maximum is", num1)
elif (num3 >= num2): print("Second Maximum is", num3)
else: print("Second Maximum is", num2)
print("End of the program...")
