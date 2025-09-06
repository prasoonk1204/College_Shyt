n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

sum = n1 + n2

# PRINTING THE OUTPUT IN DIFFERENT WAYS
# So 100 + 200 = 300

# METHOD 1
print("So", n1, "+", n2, "=", sum)

# METHOD 2
# print("So" + n1 + " + " + n2 + " = " + sum)   # TypeError: Since we are concatenating string with integers

print("So " + str(n1) + " + " + str(n2) + " = " + str(sum))

# METHOD 3
print("So {} + {} = {}".format(n1, n2, sum))

# METHOD 4
print("So {fn} + {sn} = {res}".format(fn=n1, sn=n2, res=sum))

# METHOD 5
print("So {fn} + {sn} = {res}".format(res=sum, sn=n2, fn=n1))

# METHOD 6
print("So {0} + {1} = {2}".format(n1, n2, sum))

# METHOD 7
print("So {2} + {0} = {1}".format(n2, sum, n1))

# METHOD 8
print("So %d + %d = %d"%(n1, n2, sum))

# METHOD 9
print("So %d + %f = %d"%(n1, n2, sum))

# METHOD 10
print("So %d + %8.2f = %d"%(n1, n2, sum))

# METHOD 11
print(f"So {n1} + {n2} = {sum}")











#epilectic