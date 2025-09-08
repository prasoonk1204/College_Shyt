# Swaping of 2 numbers

n1 = 100
n2 = 80
print("Before Swaping: n1 =", n1, "n2 =", n2)

n1, n2 = n2, n1
print("After Swaping: n1 =", n1, "n2 =", n2)


# Using 3rd variable
n1, n2 = 100, 200
print(n1, n2)

temp = n1 + n2
n2 = temp - n2
n1 = temp - n2
print(n1, n2)


# Without using 3rd variable
# In case of *
n1 = 100
n2 = 50
print(n1, n2)

n1 = n1 * n2
n2 = n1 // n2
n1 = n1 // n2
print(n1, n2)


# In case of +
n1 = 100
n2 = 50
print(n1, n2)

n1 = n1 + n2
n2 = n1 - n2
n1 = n1 - n2
print(n1, n2)


# In case of /
n1 = 100
n2 = 50
print(n1, n2)

n1 = n1 / n2
n2 = int(n1 * n2)
n1 = int(n2 / n1)
print(n1, n2)

# In case of -
n1 = 100
n2 = 50
print(n1, n2)

n1 = n1 - n2
n2 = n1 + n2
n1 = n2 - n1
print(n1, n2)

# In case of ^ (XOR)
n1 = 100
n2 = 50
print(n1, n2)

n1 = n1 ^ n2
n2 = n1 ^ n2
n1 = n1 ^ n2
print(n1, n2)