# Inbuilt Collections

# list of inbuilt collections
list1 = [11, True, 23.45, "College"]   # mutable
print(list1, len(list1), type(list1), id(list1))
tuple1 = (11, True, 23.45, "College")  # immutable
print(tuple1, len(tuple1), type(tuple1), id(tuple1))
dict1 = {"name":"Gagan", "age":34, "gender":"male", "location":"West Bengal"}   # mutable, collection of key and value pairs
print(dict1, len(dict1), type(dict1), id(dict1))
set1 = {"Gagan", "Male", 34, "Gagan", 34, "W.B.", "Male", "W.B.", 34}   # mutable, collection of unordered unique values
print(set1, len(set1), type(set1), id(set1))
fset1 = frozenset({"Gagan", "Male", 34, "Gagan", 34, "W.B.", "Male", "W.B.", 34})  # immutable, collection of unordered unique values
print(fset1, len(fset1), type(fset1), id(fset1))



# defining empty collections
list1 = []
print(list1, len(list1), type(list1), id(list1))
tuple1 = ()
print(tuple1, len(tuple1), type(tuple1), id(tuple1))
dict1 = {}
print(dict1, len(dict1), type(dict1), id(dict1))
set1 = set()
print(set1, len(set1), type(set1), id(set1))
fset1 = frozenset()
print(fset1, len(fset1), type(fset1), id(fset1))