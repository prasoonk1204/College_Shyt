import math

print(math.sin(0), math.cos(0), math.tan(0))
print(math.sinh(0), math.cosh(0), math.tanh(0))
print(math.factorial(6), math.factorial(7))
print(math.gcd(100, 70), math.lcm(100, 70))
print(math.e, math.pi, math.tau)
print(math.log(10), math.log(10, math.e))
print(math.log(1024, 2), math.log2(1024), math.log10(1000))
print(math.dist((10, 5), (22, 40)))
print(math.sqrt(10000), math.ceil(11.1), math.floor(11.1))


help(math.ceil)


print(math.pow(10, 3), 10. ** 3)
print(math.perm(10, 3))
print(math.comb(10, 3))
print(math.factorial(10)/(math.factorial(10-3)*math.factorial(3)))


print(abs(-10.3), abs(10.3))


myexpression = input("Please enter one expression: ")
print(myexpression)
print(eval(myexpression))