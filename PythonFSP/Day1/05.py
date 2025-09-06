# Arithmetic Operators: +, -, *, /, %, //, **
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operator: =
# Special Assignment Operators: +=, -=, *=, /=, //=, %=, **=
# Bitwise Operators: &, |, ^, ~, <<, >>, &=, |=, ^=, <<=, >>=


# Arithmetic Operators
print(150 + 80)   # addition
print(150 - 80)   # subtraction
print(150 * 80)   # multiplication
print(150 / 80)   # float division
print(150 // 80)  # integer division (floor division)
print(150 % 80)   # modulus (remainder)
print(2 ** 3)    # exponentiation (power)


# Comparison Operators
print(10 == 20, 10 == 10)   # equal to
print(10 != 20, 10!=10)   # not equal to
print(10 > 20, 30 > 20)    # greater than
print(10 < 20, 30 < 20)    # less than
print(10 >= 20, 30 >= 20)   # greater than or equal to
print(10 <= 20, 30 <= 20)   # less than or equal to

# Shell scripting for comparison: -eq, -ne, -gt, -lt, -ge, -le


# Logical Operators
print(True and True, True and False, False and False)
print(True or True, True or False, False or False)
print(not True, not False)

print(10 < 20 and 30 > 20)
print(10 < 20 or 30 < 20)


# Assignment Operator
a = 10     # variable = expression
print(a)


# Special Assignment Operators
n1 = 10
n1 += 5    # n1 = n1 + 5
print(n1)

n1 -= 10    # n1 = n1 - 5
print(n1)

n1 *= 5    # n1 = n1 * 5
print(n1)

n1 /= 5    # n1 = n1 / 5
print(n1)

n1 //= 5    # n1 = n1 // 5
print(n1)

n1 %= 5    # n1 = n1 % 5
print(n1)

# hexadecimal number system
var1 = 0x100    # 1*16^2 + 0*16^1 + 0*16^0 = 256
print(var1, type(var1))

var1 = 0xaaa    # 10*16^2 + 10*16^1 + 10*16^0 = 2730
print(var1, type(var1))


# Bitwise Operators

num1 = 100
print(num1, num1 << 2, num1 >> 2)

# 100 = 64 + 32 + 4 =  0110 0100

# 100 << 2 = 0001 1001 0000 = 256 + 128 + 16 = 400
# x << n means x * (2**n)

# 100 >> 2 = 0001 1001 = 16 + 8 + 1 = 25
# x >> n means x // (2**n)


num1 = 1
print(num1, ~num1)   # ~x means -x-1
# num1 = 1 = 0000 0001 => ~0000 0001 => 1111 1110 + 1 => -0000 0010 => -2