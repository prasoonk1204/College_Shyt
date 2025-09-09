# MAP
def funct1(par):
    return len(par)

result = map(funct1, ["Sunday", "Monday", "Tuesday", "Wednesday"])
print(result)

print(list(result))     # show the output
print(tuple(result))       # empty (since it is already traversed)


def funct2(par1, par2):
    return par1 + par2

result = map(funct1, ["Sunday", "Monday", "Tuesday", "Wednesday"])
print(list(result))

result = map(funct2, [1, 2, 3], [4, 5, 6])
print(list(result))

result = map(funct2, ["Sun", "Mo", "Tuesd"], ["day", "nday", "ay"])
print(list(result))

result = map(lambda x: len(x), ["Sunday", "Monday", "Tuesday", "Wednesday"])
print(list(result))


def funct3(par1, par2):
    return par1 * par2

result = map (funct3, ["hi", "hey", "hello"], [2, 3, 4])
print(list(result))


def funct4(marks):
    if (marks < 40): return "Poor"
    elif (marks < 60): return "Good"
    else: return "Excellent"

result = map (funct4, [30, 65, 64, 87, 75])
print(result)

result = list(map(lambda m: "poor" if (m<40) else "good"
                  if (m<60) else "excellent", [30, 65, 64, 87, 75]))
print(result)

user_input = list(map(int, input("Enter integer numbers: ").split()))
print(user_input, type(user_input), type(user_input[0]))



num1, num2, num3 = list(map(int, input("Enter numbers:").split()))
print(f"Input numbers are {num1}, {num2} and {num3}...")
if (num1 >= num2 and num1 >= num3):
    print(f"The Maximum number is {num1}...")
elif(num2 >= num3):
    print(f"The Maximum number is {num2}...")
else:
    print(f"The Maximum number is {num3}...")
print("End of the program...")


# FILTER
def funct1(age):
    if (age >= 18): return True
    else: return False

ages = [50, 17, 20, 5, 32]
adults = list(filter(funct1, ages))
print(adults)


def funct2(num):
    return True if (num % 2 == 0) else False

total_even = sum(filter(funct2, [33, 44, 55, 22, 66]))
print(total_even)
total_even = sum(filter(lambda n:True if (n % 2 == 0) else False, [33, 44, 55, 22, 66]))
print(total_even)


# function to find palindrome words from a string
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

result = filter(is_palindrome, ["Malayalam", "Python", "Madam"])
print(list(result))


def funct(num):
    if (num < 0): return False
    return num == int(num ** 0.5) ** 2

print(list(filter(funct, [100, 35, 25, 89, 16, -25])))


# REDUCE
from functools import reduce
def custom_sum(first_num, second_num):
    print(first_num, second_num)
    return first_num + second_num
    
result = reduce(custom_sum, [100, 200, 300, 400])
print(result)
result = reduce(custom_sum, [100, 200, 300, 400], 1000)
print(result)
numbers = [200, 100, 900, 400, 1000, 220]
print(reduce(lambda n1, n2: n1 if (n1 >= n2) else n2, numbers))
print(max(numbers))


# ZIP
fruits = ["mango", "banana", "pineapple", "kiwi"]
stocks = [110, 220, 440, 330]
print(zip(fruits, stocks))
print(list(zip(fruits, stocks)))
print(tuple(zip(fruits, stocks)))
print(dict(zip(fruits, stocks)))


# Cartesian Product
from itertools import product
list1 = ['mango', 'coconut']
list2 = [100, 300, 200]
print(product(list1, list2))
print(list(product(list1, list2)))
print(tuple(product(list1, list2)))
print(dict(product(list1, list2)))
print(dict(list(product(list1, list2))))


# bisect_left and bisect_right
from bisect import bisect_left
from bisect import bisect_right
list1 = [11, 22, 33, 44, 55, 66, 77, 88]
print(bisect_left(list1, 35), bisect_right(list1, 35))
print(bisect_left(list1, 65), bisect_right(list1, 65))
print(bisect_left(list1, 44), bisect_right(list1, 44))
print(bisect_left(list1, 55), bisect_right(list1, 55))


# cycle function
import itertools
var1 = itertools.cycle([100, 44.56, True, [11,22,33], (55,66,77)])
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))
print(next(var1))