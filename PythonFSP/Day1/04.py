# Dynamic variables

var1 = 100
print(var1, type(var1), id(var1))

var1 = 100.5
print(var1, type(var1), id(var1))

var1 = "100"
print(var1, type(var1), id(var1))

var1 = True
print(var1, type(var1), id(var1))

# all have different memory locations(ids)


var2 = 200
var3 = 200
var4 = var2
print(var2, id(var2), var3, id(var3), var4, id(var4))
# var2 and var3 have same value, so same memory location
# var4 is assigned to var2, so same memory location
# memory optimization is being done here by python interpreter

var1 = -7
var2 = -7
print(var1, id(var1), var2, id(var2))