def binarySearchItr(A,key):
    l = 0
    r = len(A) -1
    while l <= r:
        mid = (l+r) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            l = mid+1
        else:
            r = mid -1   
    return -1         



A = [2,5,6,7,8,9,10]            

print(binarySearchItr(A, 11))