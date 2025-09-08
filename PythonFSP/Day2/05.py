# Lambda Function
# In Python programming, a lambda function is a small anonymous function that can have any number of arguments, but can only have one expression. The expression is evaluated and returned as the function result. Lambda functions are commonly used in combination with higher-order functions such as map(), filter(), and reduce().

# Some of the properties of lambda functions in Python programming include:
# * Anonymous: Lambda functions are anonymous, meaning they do not have a name like regular functions. They are defined using the keyword "lambda" followed by the arguments and the expression.
# * Single Expression: A lambda function can only contain a single expression that is evaluated and returned as the function result. This means that it cannot contain multiple statements or control flow structures.
# * Concise: Lambda functions are concise and can be defined in a single line of code. This makes them useful for defining simple functions on-the-fly.
# * Immutable: Lambda functions are immutable, meaning they cannot be modified once defined. This means that you cannot change the behavior of a lambda function after it has been defined.
# * Higher-order Functions: Lambda functions are often used in combination with higher-order functions such as map(), filter(), and reduce(). These functions take other functions as arguments and return new functions as results.
# * Memory-efficient: Lambda functions are memory-efficient since they are defined on-the-fly and do not require a separate function definition. This can be useful when working with large data sets or when memory usage is a concern.


MySquare = lambda num: num * num
print(MySquare(10))
print(MySquare(12))
print(type(MySquare))


MyAddition = lambda num1, num2: num1 + num2
print(MyAddition(100, 200))
print(MyAddition(300, 500))
print(type(MyAddition))


MyFactorial = lambda num: 1 if (num == 0 or num == 1) else num * MyFactorial(num - 1)
print(MyFactorial(5))
print(MyFactorial(6))
print(type(MyFactorial))


MyFunction = lambda: 100 + 200
print(MyFunction())
print(type(MyFunction))


def funct10(num):
    myfunction = lambda number: num * number
    return myfunction

var20 = funct10(20)
var30 = funct10(30)
print(type(var20), type(var30))
print(var20(5))
print(var30(6))


def funct11(n, funct):
    return funct(n)
print(funct11(5, var20))
print(funct11(6, var30))


def funct12():
    i = 100
    print(i, id(i))
i = 200
print(i, id(i))
funct12()
print(i, id(i))


def funct13():
    global i
    i = 100
    print(i, id(i))
i = 200
print(i, id(i))
funct13()
print(i, id(i))
