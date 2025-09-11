# Abstract Class and Interface

# abstract class
from abc import ABC, abstractmethod    # ABC => Abstract Base Class
class AbsBaseClass(ABC):
    def __init__(self):
        print("Abstract class constructor executing...")
    @abstractmethod   # annotation or decorator
    def abstractMethod(self):
        pass
    def concreteMethod(self):
        print("Concrete method executing...")
class Derived(AbsBaseClass):
    def abstractMethod(self):
        print("Abstract method body has been redefined...")
    def function(self):
        print("Function method executing...")
ob1 = Derived()
ob1.abstractMethod()
ob1.concreteMethod()
ob1.function()



# abstract class
from abc import ABC, abstractmethod    # ABC => Abstract Base Class
class AbsBaseClass(ABC):
    def __init__(self):
        print("Abstract class constructor executing...")
    @abstractmethod   # annotation or decorator
    def abstractMethod(self):
        print("Initial Content...")
    def concreteMethod(self):
        print("Concrete method executing...")
class Derived(AbsBaseClass):
    def abstractMethod(self):
        print("Abstract method body has been redefined...")
        super().abstractMethod()
    def function(self):
        print("Function method executing...")
ob1 = Derived()
ob1.abstractMethod()
ob1.concreteMethod()
ob1.function()



# interface
from abc import ABC, abstractmethod    # ABC => Abstract Base Class
class MyInterface(ABC):
    def __init__(self):
        print("Interface class constructor executing...")
    @abstractmethod   # annotation or decorator
    def abstractMethod1(self):
        pass
    @abstractmethod   # annotation or decorator
    def abstractMethod2(self):
        pass
    @abstractmethod   # annotation or decorator
    def abstractMethod3(self):
        pass
class Derived(MyInterface):
    def abstractMethod1(self):
        print("Abstract method body-1 has been redefined...")
    def abstractMethod2(self):
        print("Abstract method body-2 has been redefined...")
    def abstractMethod3(self):
        print("Abstract method body-3 has been redefined...")
ob1 = Derived()
ob1.abstractMethod1()
ob1.abstractMethod2()
ob1.abstractMethod3()