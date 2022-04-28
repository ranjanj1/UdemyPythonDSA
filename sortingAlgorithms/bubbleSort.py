def bubbleSort(A):
    n = len(A)
    for passes in range(n-1, 0, -1):
        for i in range(passes):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp

A = [ 2,4,1,22,11,43,11,23,88]

bubbleSort(A)

print(A)