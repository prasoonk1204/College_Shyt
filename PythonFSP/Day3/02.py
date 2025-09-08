# String processing

myStr = "University"
print(myStr, len(myStr), type(myStr), id(myStr))

# string indexing
print(myStr[3], myStr[-7], myStr[6], myStr[-4])

# string slicing
print(myStr[6:], myStr[-4:], myStr[:6], myStr[:-4])

print(myStr[3:6], myStr[-7:-4], myStr[3:-4], myStr[-7:6])

print(myStr[5:2:-1], myStr[-5:-8:-1], myStr[5:-8:-1], myStr[-5:2:-1])

print(myStr[1::2], myStr[-9::2], myStr[::2], myStr[::-1])


# string methods
str1 = "ItALiaN gRaNd pRIX"

print(str1, len(str1), type(str1), id(str1))
print(str1.upper())
print(str1.lower())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
print(str1.center(50).upper())
print(str1.upper().center(50))


str2 = "college"
for ch in str2:
    print(ch, end=", ")
print()


for i in range(len(str2)):
    print(str2[i], end=", ")
print()


str3 = "HELLOWORLD"
print(str3)
print(list(str3))
print(tuple(str3))
print(set(str3))
print(frozenset(str3))


mystr = "engineering"
print(mystr)
print(mystr.find("neer"), mystr.find("Neer"), mystr.find("gin"))
print(mystr.find("neer",3,8), mystr.find("neer",3,7))
print(mystr.index("neer"))
print(mystr.upper().index("NEER"))
print(mystr.index("Neer"))


mystr = "engineering"
try:
    print(mystr.index("Neer"))
except ValueError as ve:
    print("Unsuccessful Searching...")