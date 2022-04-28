x = range(5)
print(x)  # range(0,5)
print(type(x))  # range


print(x[4])  # 0

## x[0] = 10  -- this is not possible because range function is immutable

print("---------")
y = range(0,10,2) # 0,2,4,6,8

print("---------")
for i in y:
    print(i)
 
print("---------")
z = range(10,0,-2) # 10,8,6,4,2

for i in z:
    print(i)