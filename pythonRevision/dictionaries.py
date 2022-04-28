d = {'USA': 100, 'UK': 200, 'India': 300}

print(d)
print(len(d))

print(d['India'])
d['Aus'] = 400

print(d)

del(d['Aus'])
print(d)

for i in d:
    print(i, d[i]) 

print('USA' in d)