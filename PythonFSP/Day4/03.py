# superset, subset, disjoint

set1 = {11, 22, 33}
set2 = {44, 55, 66, 77, 88, 99}
set3 = {44, 55, 99}

print(set1, len(set1), set2, len(set2), set3, len(set3))
print(set1.issuperset(set2), set2.issuperset(set3), set3.issubset(set2))

print(set1.issubset(set2), set2.issubset(set3), set3.issubset(set2))
print(set1.isdisjoint(set2), set2.isdisjoint(set3), set3.isdisjoint(set2))


# for frozenset
set1 = frozenset({11, 22, 33})
set2 = frozenset({44, 55, 66, 77, 88, 99})
set3 = frozenset({44, 55, 99})

print(set1, len(set1), set2, len(set2), set3, len(set3))
print(set1.issuperset(set2), set2.issuperset(set3), set3.issubset(set2))

print(set1.issubset(set2), set2.issubset(set3), set3.issubset(set2))
print(set1.isdisjoint(set2), set2.isdisjoint(set3), set3.isdisjoint(set2))


# insert operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
set1.add(5)
print(set1, len(set1))
set1.add(6)
print(set1, len(set1))


# delete operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
set1.remove(1)
print(set1, len(set1))
# set1.remove(5)        # throws KeyError
# print(set1, len(set1))


# discard operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
set1.discard(1)
print(set1, len(set1))
set1.discard(5)         # does not throw KeyError
print(set1, len(set1))


set1 = {1, 2, 3, 4, 5, 6, 7}
print(set1, len(set1))
set1.pop()      # deleted from the start index
print(set1, len(set1))
set1.pop()
print(set1, len(set1))

# clear operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
set1.clear()
print(set1, len(set1))


# clear operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
del set1
# print(set1, len(set1))      # throws NameError


# update operation
set1 = {1, 2, 3, 4}
print(set1, len(set1))
set1.discard(3)
set1.add(5)
print(set1, len(set1))


# copy operation
set1 = {1, 2, 3, 4, 5, 6, 7}
print(set1, len(set1))
set2 = set1     # shallow copy 
print(set2, len(set2))
set1.add(8)
print(set1, len(set1))
print(set2, len(set2))


set1 = {1, 2, 3, 4, 5, 6, 7}
print(set1, len(set1))
set2 = set1.copy()      # deep copy
print(set2, len(set2))
set1.add(8)
print(set1, len(set1))
print(set2, len(set2))


# frozenset copy operation
set1 = frozenset({1, 2, 3, 4, 5, 6, 7})
print(set1, len(set1))
set2 = set1.copy()
print(set2, len(set2))


# concatenation
set1 = {1, 2}
set2 = {1, 6, 7, 8}
print(set1, len(set1))
print(set2, len(set2))
set1.update(set2)
print(set1, len(set1))