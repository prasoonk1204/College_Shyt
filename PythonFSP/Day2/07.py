# Problem Solving 

# Find the "Digital Root" of a given integer number.

# Let n = 104 => 1 + 0 + 4 = 5 (Digital root)
# Let n = 164 => 1 + 6 + 4 = 11 => 1 + 1 = 2 (Digital root)
# Let n = 919 => 9 + 1 + 9 = 19 => 1 + 9 = 10 => 1 + 0 = 1 (Digital root)

num = int(input("Please enter one integer number: "))
total = 0
while(num != 0):
    last_digit = num % 10
    total += last_digit
    num = num // 10
    if (num == 0 and total >= 10):
        num, total = total, 0
        print("Going again with num =", num)
print("So the Digital Root is", total)
print("End of the program...")



# Find out the total of first n terms (user given) of the following series:

# place no 1   2   3   4   5    6   7   8   9   10   11  12 ...
# total =  1 + 2 + 3 + 4 + 10 + 5 + 6 + 7 + 8 + 26 + 9 + 10 + ... n terms
# What is the 99th term of the series? Answer - 80
n = int(input("Please enter the number of terms: "))
fsum = tsum = 0
term = 1
for i in range(1, n + 1):
    if (i % 5 == 0):
        fsum += tsum
        print("Adding Temporary Sum:", tsum)
        tsum = 0
    else:
        tsum += term
        fsum += term
        print("Adding Term:", term)
        term += 1
print(f"So the sum of first {n} terms is {fsum}...")
print("End of the program...")