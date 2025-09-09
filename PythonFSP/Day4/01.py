dict1 = {"apple":100, "pineapple":200, "coconut":350, "mango":100}
print(dict1, len(dict1), type(dict1), id(dict1))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

for t in dict1.items():
    print(f"Key = {t[0]} and Value = {t[1]}")

print(dict1.get("coconut"))
print(dict1["coconut"])


# print(dict1.get("orange"))      # prints None
# print(dict1.get("orange", "Not Found"))      # prints Not found
# print(dict1["orange"])      # throws KeyError

try:
    print(dict1["orange"])
except KeyError as ke:
    print("Key not found...")
    print("Error message:", ke)
    print("Error Type:", type(ke))
    
# insert operation 
dict1["banana"] = 500
print(dict1, len(dict1), type(dict1), id(dict1))

# update operation 
dict1["apple"] = 290
print(dict1, len(dict1), type(dict1), id(dict1))

# delete operation
print(dict1.pop("apple"))
print(dict1, len(dict1), type(dict1), id(dict1))

print(dict1.popitem())     # deletes last key-value pair
print(dict1, len(dict1), type(dict1), id(dict1))

dict1.setdefault("pineapple", 900)
print(dict1, len(dict1), type(dict1), id(dict1))

dict1.setdefault("lime", 650)
print(dict1, len(dict1), type(dict1), id(dict1))

del dict1
# print(dict1, len(dict1), type(dict1), id(dict1))


# concatenation of dictionaries
dict1 = {"apple":100, "pineapple":200, "coconut":350, "mango":100}
dict2 = {"banana":500, "orange":560, "grapes":700}

print("Before concatenation:")
print("Dict1:", dict1, len(dict1), type(dict1), id(dict1))
print("Dict2:", dict2, len(dict2), type(dict2), id(dict2))

dict1.update(dict2)
print("After concatenation")
print("Dict1:", dict1, len(dict1), type(dict1), id(dict1))
print("Dict2:", dict2, len(dict2), type(dict2), id(dict2))


# forming a new dictionary
fruits = ["apple", "pineapple", "coconut", "mango", "banana"]
stock = 120
dict1 = dict.fromkeys(fruits, stock)
print(dict1, len(dict1), type(dict1), id(dict1))


dict3 = {"banana":500, "orange":560, "grapes":700, "coconut":350}
dict4 = dict3    # shallow copy
print(dict3, id(dict3))
print(dict4, id(dict4))
dict4["banana"] = 600
print(dict3, id(dict3))
print(dict4, id(dict4))


dict3 = {"banana":500, "orange":560, "grapes":700, "coconut":350}
dict4 = dict3.copy()    # deep copy
print(dict3, id(dict3))
print(dict4, id(dict4))
dict4["coconut"] = 600
print(dict3, id(dict3))
print(dict4, id(dict4))


def switch_case(month_no):
    switcher = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
    return switcher.get(month_no, "Invalid month number!!!")

print(switch_case(2))
print(switch_case(12))
print(switch_case(4))
print(switch_case(20))


fruits = ["mango", "guava", "banana", "apple", "pineapple"]
stock = [100, 200, 300, 400, 500]

print(zip(fruits, stock))
print(list(zip(fruits, stock)))
print(tuple(zip(fruits, stock)))
print(dict(zip(fruits, stock)))
print(dict(list(zip(fruits, stock))))
print(list(dict(zip(fruits, stock))))