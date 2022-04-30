from distutils.archive_util import make_zipfile
from re import A


def countSort(A):
    n = len(A)
    maxSize = max(A)
    carray = [0] * (maxSize + 1)
    for i in range(n):
        carray[A[i]] = carray[A[i]] + 1
    i = 0
    j= 0
    while i < maxSize +1:
        if carray[i] > 0:
            A[j] = i
            j = j + 1
            carray[i] = carray[i] - 1
        else:
            i = i + 1    


A = [3,1,2,44,22,1,2,4,4]       

countSort(A)

print(A)