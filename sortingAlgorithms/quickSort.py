# def partition(A,low,high):
#     pivot = A[low]
#     i = low + 1   # since python doesn't have do while loop so we initialize it to low +1
#     j = high
#     while True:
#         while i <= j and A[i] <= pivot:
#             i += 1
#         while i < j and A[j] > pivot:
#             j -= 1
#         if i <= j:
#             A[i], A[j] = A[j], A[i]
#         else:
#             break  
#     A[low], A[j] = A[j], A[low]
#     return j  

# def quickSort(A,low,high):
#     if low < high:
#         pi = partition(A,low,high)
#         quickSort(A,low,pi-1)
#         quickSort(A,pi+1,high)

     

# A = [3, 5, 8, 9, 6, 2]

# quickSort(A,0,len(A)-1)

# print(A)



def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <=j and A[j] > pivot:
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)



A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
quicksort(A, 0, len(A)-1)
print('Sorted Array:',A)




