# Tuple Processing

collection1 = (11, 22, 34.45, 400, -350)
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))
print(sum(collection1), sum(collection1) / len(collection1))


collection1 = (11, 22, True, 34.45, False, 400, -350)
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))
print(sum(collection1), sum(collection1) / len(collection1))


collection1 = ("Sun", "sat", "thu", "fri")
print(collection1, len(collection1), type(collection1), id(collection1))
print(max(collection1), min(collection1))
# print(sum(collection1), sum(collection1) / len(collection1))


collection1 = (False, "Sun", "sat", True, "thu", "fri", 100, 23.45)
print(collection1, len(collection1), type(collection1), id(collection1))
# print(max(collection1), min(collection1))
# print(sum(collection1), sum(collection1) / len(collection1))


# L to R ->     0         1         2            3         4
collection1 = ("Sunday", "Friday", "Wednesday", "Monday", "Tuesday")
# R to L ->    -5        -4        -3           -2        -1
print(collection1, len(collection1), type(collection1), id(collection1))
print(collection1[4], collection1[-1]) # indexing
print(collection1[:2], collection1[:-3]) # slicing
print(collection1[3:], collection1[-2:])
print(collection1[1:4], collection1[-4:-1])
print(collection1[2][3:6], collection1[-3][-6:-3])
print(collection1[::-1])


# L to R ->      0         1         2             0         1
collection1 = (("Sunday", "Friday", "Wednesday"),("Monday", "Tuesday"))
# R to L ->     -3        -2        -1            -2        -1
print(collection1, len(collection1), type(collection1), id(collection1))
print(collection1[0], collection1[1])
print(collection1[0][1:], collection1[-2][-2:])
print(collection1[0][2][3:6], collection1[-2][-1][-6:-3])
print(collection1[1][1][2:5], collection1[-1][-1][-5:-2])


# tuple concatenation
collection1 = (100, 30, 200, 400)
collection2 = (222, 444, 333)
print(collection1, len(collection1))
print(collection2, len(collection2))
collection3 = collection1 + collection2
print(collection3, len(collection3))


# tuple of tuples
collection1 = (100, 30, 200, 400)
collection2 = (222, 444, 333)
print(collection1, len(collection1))
print(collection2, len(collection2))
collection3 = (collection1, collection2)
print(collection3, len(collection3), len(collection3[0]), len(collection3[1]))


tuple1 = ('red', 'green', 'blue', 'magenta', 'red', 'green', 'blue', 'silver')
print(tuple1, len(tuple1))
print(tuple1.count('blue'), tuple1.count('brown'))
try:
    print(tuple1.index('green'), tuple1.index('green', 0), tuple1.index('green', 2))
    print(tuple1.index('green', 6))
except ValueError as ve:
    print("Unsuccessful searching...")


var1 = (10)
print(var1, type(var1))     # gives type as "int"

var1 = (10,)        # singleton represenatation of a tuple
print(var1, type(var1))


# Problem on Piglatin word generator:
# Input_String = "mohan das karam chand gandhi"
# Output_String = "ohanmp asdp aramkp handcp andhigp"

str1 = "mohan das karam chand gandhi"

# words = str1.split()
# output = []

# for word in words:
#     if len(word) > 1:
#         piglatin = word[1:] + word[0] + 'p'
#     else:
#         piglatin = word + 'p'
#     output.append(piglatin)

# output_string = ' '.join(output)
# print("Output:", output_string)


output_str = ""
for words in str1.split():
    output_str += words[1:] + words[0] + "p "
output_str = output_str.strip()
print("Output:", output_str)


# Plain Text: transfer one million dollars to my swiss bank account six two two
# Encrypted Text: wudqvihu rqh ploolrq glooduv wr pb vzlvv edqn dffrxqw vla wzr wzr

# abcdefghijklmnopqrstuvwxyx
# defghijklmnopqrstuvwxyxabc

input_str = "transfer one million dollars to my swiss bank account six two two"
output_str = ""

for char in input_str:
    if char.isalpha():
        if (char.lower() >= 'a' and char.lower() <= 'w'): char = chr(ord(char) + 3)
        else: char = chr(ord(char) - 23)
    output_str += char

print("Output:", output_str)