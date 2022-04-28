from math import floor
def binarySearchRec(A, key, l, r):
    if l > r:
        return -1
    else:
        mid = floor((l+r)/2)
        if key == A[mid]:
            return mid
        elif key > A[mid]:
            return binarySearchRec(A,key, mid+1, r )
        else:
            return binarySearchRec(A,key, l, mid-1 )    

A = [2,5,6,7,8,9,10]    


print(binarySearchRec(A,11,0,6))