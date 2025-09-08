# Patterns

# pattern - 1
# n = 6 (user given)
#                  i   .   *
#                -------------
# .....*           1   5   1      (i, n)
# ....***          2   4   3 . => (n - i)
# ...*****         3   3   5
# ..*******        4   2   7 * => (2 * i - 1)
# .*********       5   1   9
# ***********      6   0  11 
#                -------------
#                Tracing Table

n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print("." * (n - i) + "*" * (2 * i - 1))
print("End of the program...")


# pattern - 2
# n = 6 (user given)
#                  i   .   *
#                -------------
# ***********      1   0  11      (i, n)
# .*********       2   1   9 . => (i - 1)
# ..*******        3   2   7
# ...*****         4   3   5 * => (2 * (n - i) + 1)
# ....***          5   4   3
# .....*           6   5   1 
#                -------------
#                Tracing Table

n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print("." * (i - 1) + "*" * (2 * (n - i) + 1))
print("End of the program...")


# pattern - 3
# n = 11 (user given ODD integer number)   m = (n + 1) // 2 = 6
#                  i   .   *
#                -------------
# .....*           1   5   1      (i, m, n)
# ....***          2   4   3 . => (m - i)
# ...*****         3   3   5
# ..*******        4   2   7 * => (2 * i - 1)
# .*********       5   1   9
# ***********    __6___0__11__
# .*********       7   1   9
# ..*******        8   2   7 . => (i - m)
# ...*****         9   3   5
# ....***         10   4   3 * => (2 * (n - i) + 1)
# .....*          11   5   1
#                -------------
#                Tracing Table

while(True):
    n = int(input("Please enter an ODD integer for number of layers:"))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    if (i <= m): b = (m - i); s = (2 * i - 1)
    else: b = (i - m); s = (2 * (n - i) + 1)
    print("." * b + "*" * s)
print("End of the program...")


# pattern - 4
# n = 11 (user given ODD integer number)   m = (n + 1) // 2 = 6
#                  i   .   *
#                -------------
# ***********      1   0  11      (i, m, n)
# .*********       2   1   9 . => (i - 1)
# ..*******        3   2   7
# ...*****         4   3   5 * => (2 * (m - i) + 1)
# ....***          5   4   3
# .....*         __6___5___1__
# ....***          7   4   3
# ...*****         8   3   5 . => (n - i)
# ..*******        9   2   7
# .*********      10   1   9 * => (2 * (i - m) + 1)
# ***********     11   0  11
#                -------------
#                Tracing Table

while(True):
    n = int(input("Please enter an ODD integer for number of layers:"))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    if (i <= m): b = (i - 1); s = (2 * (m - i) + 1)
    else: b = (n - i); s = (2 * (i - m) + 1)
    print("." * b + "*" * s)
print("End of the program...")


# pattern - 5
# n = 6 (user given)
#                  i   .   Char
#                -------------
# .....A           1   5   A      (i, n)
# ....BBB          2   4   B . => (n - i)
# ...CCCCC         3   3   C
# ..DDDDDDD        4   2   D * => (2 * i - 1) Char => chr(64 + i)
# .EEEEEEEEE       5   1   E
# FFFFFFFFFFF      6   0   F 
#                -------------
#                Tracing Table

n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print("." * (n - i) + chr(64 + i) * (2 * i - 1))
print("End of the program...")


# pattern - 6
# n = 6 (user given)
#                  i   .   Char
#                -------------
# .....A           1   5   A      (i, n)
# ....BCD          2   4   B . => (n - i)
# ...CDEFG         3   3   C
# ..DEFGHIJ        4   2   D * => (2 * i - 1) Char => ???
# .EFGHIJKLM       5   1   E
# FGHIJKLMNOP      6   0   F 
#                -------------
#                Tracing Table

n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print("." * (n - i), end = "")
    for j in range(0, 2 * i - 1):
        print(chr(64 + i + j), end = "")
    print()
print("End of the program...")


# pattern - 7
# n = 9 (user given ODD integer number)  m = (n + 1) // 2 = 5

#      1  2  3  4  5  6  7  8  9       i   ll   ul
# --------------------------------    -------------
# 1 |  1  1  1  1  1  1  1  1  1       1    1    9        (i, m, n)
# 2 |  1  2  2  2  2  2  2  2  1       2    2    8  ll => i
# 3 |  1  2  3  3  3  3  3  2  1       3    3    7
# 4 |  1  2  3  4  4  4  3  2  1       4    4    6  ul => (n - i + 1)
# 5 |  1  2  3  4  5  4  3  2  1     __5____5____5__
# 6 |  1  2  3  4  4  4  3  2  1       6    4    6
# 7 |  1  2  3  3  3  3  3  2  1       7    3    7  ll => (n - i + 1)
# 8 |  1  2  2  2  2  2  2  2  1       8    2    8
# 9 |  1  1  1  1  1  1  1  1  1       9    1    9  ul => i
# --------------------------------    -----------

while(True):
    n = int(input("Please enter ODD integer number:"))
    if (n % 2 == 1): break
m = (n + 1) // 2
for i in range(1, n + 1):
    if (i <= m): ll = i; ul = (n - i + 1)
    else: ll = (n - i + 1); ul = i
    number = 1
    for j in range(1, n + 1):
        print("%4d"%number, end = "")
        if (j < ll): number += 1
        elif (j >= ul): number -= 1
    print()
print("End of the program...")