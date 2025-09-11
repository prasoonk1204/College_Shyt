# # Happy Number Problem

# from abc import ABC, abstractmethod

# # -------------------------
# # Abstract Base Class
# # -------------------------
# class HappyNumberBase(ABC):

#     @abstractmethod
#     def sum_of_squares(self, n):
#         pass

#     @abstractmethod
#     def is_happy(self, num):
#         pass


# # -------------------------
# # Concrete Class : HappyNumber
# # -------------------------
# class HappyNumber(HappyNumberBase):
#     def __init__(self, number):
#         self.__number = number
#         self.__is_happy = None   # will be computed later

#     # --- Getters ---
#     def get_number(self):
#         return self.__number

#     def get_is_happy(self):
#         return self.__is_happy

#     # --- Sum of squares of digits ---
#     def sum_of_squares(self, n):
#         total = 0
#         while n > 0:
#             digit = n % 10
#             total += digit * digit
#             n //= 10
#         return total

#     # --- Check if a number is happy ---
#     def is_happy(self, num):
#         seen = set()
#         for _ in range(100):
#             num = self.sum_of_squares(num)
#             if num == 1:
#                 return True
#             if num in seen:
#                 return False
#             seen.add(num)
#         return False

#     # --- Run check and store result ---
#     def check(self):
#         self.__is_happy = self.is_happy(self.__number)

#     # --- Display Number Status ---
#     def display(self):
#         status = "Happy" if self.__is_happy else "Unhappy"
#         print(f"Number {self.__number} is {status}.")


# # -------------------------
# # Aggregation Class : HappyRange
# # -------------------------
# class HappyRange:
#     def __init__(self, start, end):
#         self.__numbers = [HappyNumber(i) for i in range(start, end + 1)]

#     # --- Compute results for all numbers ---
#     def process(self):
#         for num in self.__numbers:
#             num.check()

#     # --- Return only happy numbers ---
#     def get_happy_numbers(self):
#         return [num.get_number() for num in self.__numbers if num.get_is_happy()]

#     # --- Display all results ---
#     def display_range(self):
#         print("\nResults for range:")
#         for num in self.__numbers:
#             num.display()


# # -------------------------
# # Main Program
# # -------------------------
# hr = HappyRange(1, 100)
# hr.process()

# print(f"\n🎉 Happy Numbers between 1 and 100:")
# print(hr.get_happy_numbers())

# hr.display_range()


def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10  
        total += digit * digit
        n //= 10   
    return total


def is_happy(num):
    seen = set() 
    for _ in range(100):
        num = sum_of_squares(num)
        if num == 1:
            return True
        if num in seen: 
            return False
        seen.add(num)
    return False 


# Find all happy numbers from 1 to 100
happy_numbers = []
for i in range(1, 101):
    if is_happy(i):
        happy_numbers.append(i)

print("Happy numbers between 1 and 100 are:")
print(happy_numbers)

