mystr = "    engineering      college   "
print(mystr, len(mystr))
print(mystr.lstrip(), len(mystr.lstrip()))
print(mystr.rstrip(), len(mystr.rstrip()))
print(mystr.strip(), len(mystr.strip()))


mystr = "#@###engineering#@##college#@##"
print(mystr, len(mystr))
print(mystr.lstrip("#@"), len(mystr.lstrip("#@")))
print(mystr.rstrip("#@"), len(mystr.rstrip("#@")))
print(mystr.strip("#@"), len(mystr.strip("#@")))


mystr = "charity begins at home"
print(mystr)
print(mystr.startswith("cha"), mystr.startswith("Cha"))
print(mystr.startswith("beg"), mystr.startswith("beg", 8, 200))
print(mystr.startswith("beg", 8, 10), mystr.startswith("beg", 8, 11))


mystr = "charity begins at home"
print(mystr)
print(mystr.endswith("home"), mystr.endswith("Home"))
print(mystr.endswith("begins"), mystr.endswith("begins", 3, 14))
print(mystr.endswith("begins", 3, 13), mystr.endswith("begins", 3, 15))


mystr = "charity begins at home"
print(mystr)
print(mystr.split())
print(mystr.split(" "))
print(mystr.split("i"))
print(mystr.split("it"))


mystr = "charity begins at home"
print(mystr)
mywords = mystr.split(" ")
print(mywords)
outputstr = " ".join(mywords)
print(outputstr)
outputstr = " - ".join(mywords)
print(outputstr)


mystr = "university"
print(mystr, mystr.count("i"), mystr.count("ver"), mystr.count("I"))


mystr = "university"
print(mystr.replace("i", "x"))
print(mystr.replace("i", "xyz"))
print(mystr)
mystr = mystr.replace("i", "xyz")
print(mystr)
print(mystr.replace("U", "pqrs"))


mystr = "   "
print(mystr, mystr.isspace())
mystr = "   city   "
print(mystr, mystr.isspace())


mystr = "university"
print(mystr, mystr.isalpha(), mystr.isalnum(), mystr.isnumeric(), mystr.isdecimal())
mystr = "1234"
print(mystr, mystr.isalpha(), mystr.isalnum(), mystr.isnumeric(), mystr.isdecimal())
mystr = "university1234"
print(mystr, mystr.isalpha(), mystr.isalnum(), mystr.isnumeric(), mystr.isdecimal())
mystr = "university@1234"
print(mystr, mystr.isalpha(), mystr.isalnum(), mystr.isnumeric(), mystr.isdecimal())
mystr = "五"
print(mystr, mystr.isalpha(), mystr.isalnum(), mystr.isnumeric(), mystr.isdecimal())