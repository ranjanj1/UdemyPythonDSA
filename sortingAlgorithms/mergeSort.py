def mergeSort(A,left,right):
    if left < right:
        mid = (left+right) //2
        mergeSort(A, left, mid)
        mergeSort(A, mid+1, right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    i = left
    j = mid+1
    k = left
    B = [0] * (right+1)

    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1    
    while i <= mid:
        B[k] = A[i]
        k += 1
        i += 1
    while j <= right:
        B[k] = A[j]
        k += 1
        j += 1

    for m in range(left, right+1):
        A[m] = B[m]


A = [0,2,0,0,1,12,13,55,11,22,1,4,6]
mergeSort(A,0, len(A)-1)
print(A)



