# Dealing with Inheritance

# # single inheritance
# class Base:
#     def __init__(self):
#         print("Base: Constructor method...")
#     def displayB(self):
#         print("Base: Display method...")
# class Derived(Base):
#     def __init__(self):
#         print("Derived: Constructor method...")
#         Base.__init__(self)
#         super().__init__()
#         super(Derived, self).__init__()
#     def displayD(self):
#         print("Derived: Display method...")
# ob1 = Derived()
# Base.__init__(ob1)
# super(Derived, ob1).__init__()
# ob1.displayB()
# ob1.displayD()



# # hierarchical inheritance
# class Base:
#     def __init__(self):
#         print("Base: Constructor method...")
#     def displayB(self):
#         print("Base: Display method...")
# class Derived1(Base):
#     def __init__(self):
#         print("Derived1: Constructor method...")
#     def displayD1(self):
#         print("Derived1: Display method...")
# class Derived2(Base):
#     def __init__(self):
#         print("Derived2: Constructor method...")
#     def displayD2(self):
#         print("Derived2: Display method...")
# ob1 = Derived1()
# ob1.displayB()
# ob1.displayD1()
# print("-------------------------------------------")
# ob2 = Derived2()
# ob2.displayB()
# ob2.displayD2()



# # multiple inheritance
# class Base1:
#     def __init__(self):
#         print("Base1: Constructor method...")
#     def displayB1(self):
#         print("Base1: Display method...")
#     def function(self):
#         print("Base1: Function method...")
# class Base2():
#     def __init__(self):
#         print("Base2: Constructor method...")
#     def displayB2(self):
#         print("Base2: Display method...")
#     def function(self):
#         print("Base2: Function method...")
# class Derived(Base2, Base1):  # MRO => Method Resolution Order
#     def __init__(self):
#         print("Derived: Constructor method...")
#     def displayD(self):
#         print("Derived: Display method...")
# ob1 = Derived()
# ob1.displayB1()
# ob1.displayB2()
# ob1.displayD()
# ob1.function()


# Assignment
class Base:
    def _init_(self):
        print("Base: Constructor method...")

    def displayB(self):
        print("Base: Display method...")

class Derived1(Base):
    def _init_(self):
        super()._init_()
        print("Derived1: Constructor method...")

    def displayD1(self):
        print("Derived1: Display method...")

class Derived2(Base):
    def _init_(self):
        super()._init_()
        print("Derived2: Constructor method...")

    def displayD2(self):
        print("Derived2: Display method...")

class Derived3(Derived1, Derived2):
    def _init_(self):
        super()._init_()
        print("Derived3: Constructor method...")

    def displayD3(self):
        print("Derived3: Display method...")

ob = Derived3()
ob.displayB()
ob.displayD1()
ob.displayD2()
ob.displayD3()