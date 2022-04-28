from cv2 import line


import time
start = time.time()
def linearsearch(A,key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index += 1    
    return -1    

A = [10,45,23,75,36]    

print(linearsearch(A,100))
end = time.time()
print(end-start)