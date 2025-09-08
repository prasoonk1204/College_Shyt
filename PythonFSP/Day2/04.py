# User Defined Functions

def funct1():
    print("Hello !!! " * 3)
funct1()
funct1()
funct1()


def funct2(msg, times):  # positional parameters
    print(msg * times)
funct2("Welcome ", 10)   # positional arguments
funct2("Hi !!! ", 5)
funct2("Hey !!! ", 6)


def funct3(msg, times):
    return msg * times   # returns a string
print(funct3("Welcome ", 8))
print(funct3("Hi !!! ", 5))
result = funct3("Hey !!! ", 4)
print(result)
print(type(funct3))
print(type(funct3("abc", 10)))


# parameters with default arguments
def funct4(par1 = 111, par2 = 222, par3 = 333):
    print(f"par1 = {par1}, par2 = {par2} and par3 = {par3}...")

funct4(100, 200, 300)
funct4(par3 = 300, par2 = 200, par1 = 100)
funct4(100, 200)
funct4(par2 = 200, par1 = 100)
funct4(100)
funct4()
funct4(par3 = 300, par1 = 100)



def funct5(par1, par2 = None):
    # if (par2 is None): return 2 * par1
    if (par2 == None): return 2 * par1
    else: return par1 + par2

print(funct5(100, 900))
print(funct5(100))



# function with variable number of arguments
def funct6(*args):     # forcefully defining args is of tuple type
    print(args, type(args), len(args), id(args))
funct6("Rupa")
funct6("Rupa", "Bangalore")
funct6("Rupa", "Bangalore", "IBM", "Developer")
funct6("Rupa", "Bangalore", "IBM", "Developer", "72000")


# function with variable number of arguments
def funct7(**kwarg):     # forcefully defining kwarg is of dictionay type
    print(kwarg, type(kwarg), len(kwarg), id(kwarg))
funct7(name="Rupa")
funct7(name="Rupa", location="Bangalore")
funct7(name="Rupa", location="Bangalore", company="IBM")
funct7(name="Rupa", location="Bangalore", company="IBM", job="Developer", salary="72000")


# function with variable number of arguments
def funct8(*args, **kwarg):     # forcefully defining kwargs is of dictionay type
    print(args, type(args), len(args), id(args))
    print(kwarg, type(kwarg), len(kwarg), id(kwarg))
    print()
    
funct8("Rupa", "Bangalore", "IBM", job="Developer", salary="72000")
funct8("Rupa", "Bangalore", "IBM")
funct8(job="Developer", salary="72000")


# function returning multiple arguments
def funct9(num1, num2):
    total = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    quotient = num1 / num2
    remainder = num1 % num2
    return total, difference, product, quotient, remainder
n1, n2 = 100, 40
tt, dd, pp, qq, rr = funct9(n1, n2)
print(n1, n2, tt, dd, pp, qq, rr)
result = funct9(n1, n2)
print(result, len(result), type(result), id(result))
print(n1, n2, result[0], result[1], result[2], result[3], result[4])


# non-recursive factorial calculation function
def factorial_nr(num):
    if (num == 0 or num == 1): return 1
    fact = num
    for i in range(2, num):
        fact = fact * i
        print("Executing...")
    return fact
n = 6
print(n, factorial_nr(6))


# recursive factorial calculation function
def factorial_r(num):
    if (num == 0 or num == 1): return 1  # base case: for certain inputs, outputs are pre-known
    return num * factorial_r(num - 1) # recursive case: where the function will call itself
n = 6
print(n, factorial_r(6))


# fact(5) => 5 * fact(4)
#                        4 * fact(3)
#                                   3 * fact(2)
#                                               2 * fact(1)
#                                                   1
#                                       2
#                            6
#                 24
#             120