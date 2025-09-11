# Operator Overloading
var1 = 100
var2 = 40

print(var1 + var2, var1.__add__(var2))
print(var1 - var2, var1.__sub__(var2))
print(var1 * var2, var1.__mul__(var2))
print(var1 / var2, var1.__truediv__(var2))
print(var1 // var2, var1.__floordiv__(var2))
print(int.__add__(var1, var2))


class MyClass:
    def __init__(self, xx, yy):
        self.x, self.y = xx, yy

    def __str__(self):
        return f"So x = {self.x} and y = {self.y}"
    
    def __add__(self, data):
        temp = MyClass(0, 0)
        temp.x = self.x + data.x
        temp.y = self.y + data.y
        return temp
    
    def __mul__(self, data):
        temp = MyClass(0, 0)
        temp.x = self.x * data.x
        temp.y = self.y * data.y
        return temp
    
    def __gt__(self, data):
        return self.x + self.y > data.x + data.y

ob1 = MyClass(11, 22)
ob2 = MyClass(100, 200)

print(ob1, type(ob1))
print(ob2, type(ob2))

# object addition
result = ob1 + ob2   
print(result)

result = ob1.__add__(ob2)
print(result)

# object multiplication
result = ob1 * ob2
print(result)

result = ob1.__mul__(ob2)
print(result)

# object comparison
result = ob1 > ob2
print(result)

result = ob1.__gt__(ob2)
print(result)