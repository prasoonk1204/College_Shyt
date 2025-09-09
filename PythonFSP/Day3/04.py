collection1 = [11, 22, 34.45, 400, -350]
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))
print(sum(collection1), sum(collection1) / len(collection1))


collection1 = [11, 22, True, 34.45, False, 400, -350]
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))
print(sum(collection1), sum(collection1) / len(collection1))


collection1 = ["Sun", "sat", "thu", "fri"]
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))


collection1 = [False, "Sun", "sat", True, "thu", "fri", 100, 23.45]
print(collection1, len(collection1), type(collection1), id(collection1))
# print(max(collection1), min(collection1))
# print(sum(collection1), sum(collection1) / len(collection1))


# L to R ->     0         1         2            3         4
collection1 = ["Sunday", "Friday", "Wednesday", "Monday", "Tuesday"]
# R to L ->    -5        -4        -3           -2        -1
print(collection1, len(collection1), type(collection1), id(collection1))
print(collection1[4], collection1[-1]) # indexing
print(collection1[:2], collection1[:-3]) # slicing
print(collection1[3:], collection1[-2:])
print(collection1[1:4], collection1[-4:-1])
print(collection1[2][3:6], collection1[-3][-6:-3])
print(collection1[::-1])


# L to R ->      0         1         2             0         1
collection1 = [["Sunday", "Friday", "Wednesday"],["Monday", "Tuesday"]]
# R to L ->     -3        -2        -1            -2        -1
print(collection1, len(collection1), type(collection1), id(collection1))
print(collection1[0], collection1[1])
print(collection1[0][1:], collection1[-2][-2:])
print(collection1[0][2][3:6], collection1[-2][-1][-6:-3])
print(collection1[1][1][2:5], collection1[-1][-1][-5:-2])


# list concatenation
collection1 = [100, 30, 200, 400]
collection2 = [222, 444, 333]
print(collection1, len(collection1))
print(collection2, len(collection2))
collection3 = collection1 + collection2
print(collection3, len(collection3))
collection1.extend(collection2)
print(collection1, len(collection1))
print(collection2, len(collection2))


# list of lists
collection1 = [100, 30, 200, 400]
collection2 = [222, 444, 333]
print(collection1, len(collection1))
print(collection2, len(collection2))
collection3 = [collection1, collection2]
print(collection3, len(collection3), len(collection3[0]), len(collection3[1]))


# insert operation on a list
list1 = ['red', 'green', 'blue']
print(list1, len(list1))
list1.append('brown')
print(list1, len(list1))
list1.append('magenta')
print(list1, len(list1))
list1.insert(3, 'purple')
print(list1, len(list1))
list1.insert(0, 'cyan')
print(list1, len(list1))


# update operation on a list
list1 = ['red', 'green', 'blue', 'magenta', 'silver']
print(list1, len(list1))
list1[0] = 'deep red'
print(list1, len(list1))
list1[3] = 'golden'
print(list1, len(list1))


# delete operation on a list
list1 = ['red', 'green', 'blue', 'magenta', 'silver']
print(list1, len(list1))
del list1[2]
print(list1, len(list1))
del list1
print(list1, len(list1))


list1 = ['red', 'green', 'blue', 'magenta', 'silver']
print(list1, len(list1))
list1.clear()
print(list1, len(list1))


list1 = ['red', 'green', 'blue', 'magenta', 'silver']
print(list1, len(list1))
print(list1.pop())
print(list1, len(list1))
print(list1.pop())
print(list1, len(list1))
print(list1.pop())
print(list1, len(list1))


list1 = ['red', 'green', 'blue', 'magenta', 'silver']
print(list1, len(list1))
print(list1.pop(1))
print(list1, len(list1))
print(list1.pop(3))
print(list1, len(list1))
print(list1.pop(1))
print(list1, len(list1))