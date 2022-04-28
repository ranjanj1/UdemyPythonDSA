# Integer datatype

print("-----------------------------------")

a = 10
print(type(a))
print(id(a))
b = 12
print(id(b))

b = a
print(id(b))

print("-----------------------------------")

# Float dataype 

f = 2.45
fNegative = -2.45
print(type(f))
print(type(fNegative))

print("-----------------------------------")

# String datatype

s = "It's goof to learn programing "   # single line string
sMulti = '''This is 
multi line string '''

print(s)
print(type(s))

print(sMulti)
print(type(sMulti))


print("-----------------------------------")

#boolean dataype 

x = 10
y = 20 
z = x>y

print(type(x))
print(type(y))
print(type(z))
print(z)

print("-----------------------------------")


print("----------NoneDataType-----------")

a = None
print(type(a))
 

print("--------to print all keyword in Python--------")

import keyword
print(keyword.kwlist)
 
 