# List Sorting

list1 = [10, 2, -3, 40]
list2 = [14, -22, 8, -10]
list3 = [6, -7, 10, 1]
final_list = []
for i in range(len(list1)):
    final_list.append([list1[i], list2[i], list3[i]])
print(final_list)
final_list = sorted(final_list, key = lambda v: v[-1])
print(final_list)
final_list.sort(key = lambda arr: arr[-1])
print(final_list)


# List Comprehension
# List comprehenion is a complete substitute to for loops, lambda function and as well as the functions like map(), filter() and reduce().

list1 = []
for x in range(10):
    list1.append(x ** 2)
print(list1)

# list comprehension
list1 = [x ** 2 for x in range(10)]
print(list1)


list1 = []
for x in range(10):
    list1.append(2 ** x)
print(list1)

# list comprehension
list1 = [2 ** x for x in range(10)]
print(list1)


list1 = [11, 22, 33, 55, 44, 77, 66, 99, 88]
list2 = []
for x in list1:
    if (x % 2 == 0):
        list2.append(x)
print(list2)

# list comprehension
list2 = [x for x in list1 if x % 2 == 0]
print(list2)


list1 = [11, 33, 22, 66, 44, 55, 126, 77]
list2 = []
for x in list1:
    if (x % 2 == 0):
        if (x % 3 == 0):
            list2.append(x)
print(list2)

# list comprehension
list2 = [x for x in list1 if x % 2 == 0 if x % 3 == 0]
print(list2)
list2 = [x for x in list1 if x % 2 == 0 and x % 3 == 0]
print(list2)


list1 = [20, 30, 10, 60, 70, 25, 90, 100]
list2 = []
for x in list1:
    if (x >= 50):
        list2.append(x + 500)
    else:
        list2.append(x + 200)
print(list2)

# list comprehension
list2 = [x + 500 if (x >= 50) else x + 200 for x in list1]
print(list2)



# flatten a matrix
list1 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]
list2 = []
for temp_list in list1:
    for item in temp_list:
        list2.append(item)
print(list2)

# list comprehension
list2 = [item for temp_list in list1 for item in temp_list]
print(list2)


# transpose of a matrix
matrix = [[11, 22, 33, 44], [55, 66, 77, 88], [99, 11, 33, 66]]
list1 = []
for i in range(4):
    temp_list = []
    for j in range(3):
        temp_list.append(matrix[j][i])
    list1.append(temp_list)
print(list1)

# list comprehension
list1 = [[row[i] for row in matrix] for i in range(4)]
print(list1)


list1 = []
for x in range(3):
    temp_list = []
    for y in range(4):
        temp_list.append(0)
    list1.append(temp_list)
print(list1)

# list comprehension
list1 = [[0 for col in range(4)] for row in range(3)]
print(list1)


list1 = []
for x in range(4):
    temp_list = []
    for y in range(x):
        temp_list.append(0)
    list1.append(temp_list)
print(list1)

# list comprehension
list1 = [[0 for col in range(row)] for row in range(4)]
print(list1)


# replacing map() function in combination of lambda function
list1 = [11, 22, 33, 44, 55, 66, 77]
list2 = list(map(lambda x: 2 * x, list1))
print(list2)

# list comprehension
list2 = [2 * x for x in list1]
print(list2)


# replacing filter function
list1 = [11, 22, 33, 44, 55, 66, 77, 88]
oddnum_list = list(filter(lambda x: x % 2, list1))
print(oddnum_list)

# list comprehension
oddnum_list = [x for x in list1 if (x % 2)]
print(oddnum_list)


# replacing reduce function
from functools import reduce
list1 = [11, 22, 33, 44, 55, 66]
print(sum(list1))
result = reduce(lambda x, y: x + y, list1)
print(result)

# list comprehension
result = sum([x for x in list1])
print(result)