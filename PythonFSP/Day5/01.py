class MyClass:
    pass    # statement placeholder
ob1 = MyClass()
print(ob1)


class MyClass:
    '''
    This is the document string
    contains the definition and purpose of the class
    '''
ob1 = MyClass()
print(ob1.__doc__)
print(MyClass.__doc__)


mystr = "university"
print(mystr, type(mystr))
print(mystr.__doc__)
print(str.__doc__)


class MyClass:
    """This is a doc string..."""
    class_var1 = 100    # class/static variable
    def __init__(self, data1):  # constructor method, self => object binding variable
        print("Executing the constructor method...")
        self.inst_var1 = data1  # instance variable
    def display(self):
        print("Display method executing...")
        print(f"Self = {self}...")
        print(f"Class variable = {MyClass.class_var1} and {self.class_var1}...")
        print(f"Instance variable = {self.inst_var1}...")
ob1 = MyClass(111)
print(ob1.__doc__)
print(MyClass.__doc__)
print(ob1)
ob1.display()


class MyClass:
    class_var1 = 100    # class/static variable
    def __init__(self, data1):  # constructor method, self => object binding variable
        print("Executing the constructor method...")
        self.inst_var1 = data1  # instance variable
    def display(self):
        print("Display method executing...")
        print(f"Class variable = {MyClass.class_var1} and {self.class_var1}...")
        print(f"Instance variable = {self.inst_var1}...")
    def update(self):
        print("Update method executing...")
        MyClass.class_var1 += 100
        self.inst_var1 += 100
    def __str__(self):
        return "Object is getting printed..."
ob1 = MyClass(111)
ob2 = MyClass(222)
ob1.display()
ob2.display()
ob1.update()
ob1.display()
ob2.display()
print(ob1)
print(ob1.__str__())


class MyClass:
    class_var1 = 100    # class/static variable
    def __init__(self, data1):  # constructor method, self => object binding variable
        print("Executing the constructor method...")  # constructor method executes when object is created
        self.inst_var1 = data1  # instance variable
    def display(self):
        print("Display method executing...")
        print(f"Class variable = {MyClass.class_var1} and {self.class_var1}...")
        print(f"Instance variable = {self.inst_var1}...")
    def __del__(self):   # destructor method executes when object is deleted
        print("Destructor method is executing...")
ob1 = MyClass(111)
ob2 = MyClass(222)
ob1.display()
ob2.display()


# del ob1

# del ob2

# ob1.display()


# counting number of objects defined under a class
class MyClass:
    object_count = 0
    def __init__(self):
        MyClass.object_count += 1
ob1 = MyClass()
ob2 = MyClass()
ob3 = MyClass()
ob4 = MyClass()
ob5 = MyClass()
print(f"Total number of objects defined is {MyClass.object_count}...")


# there are three method types: instance, class and static methods
class MyClass:
    classVar = 111   # class variable
    # instance method
    def instMethod(self):
        print("Executing instance method", self)
        self.instVar = 100  # instance variable
        MyClass.classVar = 222  # class variable
        print(f"classVar = {MyClass.classVar} and instVar = {self.instVar}...")
    # class method
    @classmethod   # decorator or annotation
    def classMethod(cla):
        print("Executing class method", cla)
        cla.classVar = 333
        print(f"classVar = {MyClass.classVar} and classVar = {cla.classVar}...")
    # static method
    @staticmethod   # decorator or annotation
    def staticMethod():
        print("Executing static method")
        MyClass.classVar = 444
        print(f"classVar = {MyClass.classVar}...")
ob1 = MyClass()
ob1.instMethod()
MyClass.instMethod(ob1)
ob1.classMethod()
MyClass.classMethod()
ob1.staticMethod()
MyClass.staticMethod()


# built-in Python methods
class MyClass1:
    def __init__(self):
        print("Hello")
class MyClass2:
    classVar1 = 100
    def __init__(self):
        self.instVar1 = 111
    def function1(self):
        print("function1() is executing...")
        print("instVar1 =", self.instVar1)
class MyClass3(MyClass2):
    '''This is a document string...'''
    def function2(self):
        print("function2() is executing...")
    def __str__(self):
        return "I am __str__() method executing..."
ob1 = MyClass3()
ob1.function1()
ob1.function2()
print(isinstance(ob1, MyClass1), isinstance(ob1, MyClass2), isinstance(ob1, MyClass3))
print(hasattr(ob1, "classVar1"), hasattr(ob1, "instVar1"), hasattr(ob1, "abcd"))
print(getattr(ob1, "classVar1"), getattr(ob1, "instVar1"))
setattr(ob1, "instVar1", 222)
setattr(ob1, "instVar2", 333)
print(ob1.instVar1, ob1.instVar2)
print(issubclass(MyClass3, MyClass2), issubclass(MyClass3, MyClass1))
print(ob1.__str__())
print(ob1)


var1 = 100
print(var1, type(var1))
print(isinstance(var1, int), isinstance(var1, str))


print(vars(ob1))   # returns dictionary of all instance variables
print(dir(ob1))    # returns list of all attributes of an object
print(ob1.__doc__) # returns the doc string
print(ob1.__str__())  # executes __str__() method
print(ob1.__dict__) # returns dictionary of all instance variables


# dealing with private and public members
class MyClass:
    def __init__(self):
        self.publicVar = 111
        self.__privateVar = 222
    def publicMethod(self):
        print("publicMethod() is executing...")
    def __privateMethod(self):
        print("__privateMethod() is executing...")
ob1 = MyClass()
print(ob1.publicVar)
# print(ob1.__privateVar)
print(ob1._MyClass__privateVar)
ob1.publicMethod()
# ob1.__privateMethod()
ob1._MyClass__privateMethod()