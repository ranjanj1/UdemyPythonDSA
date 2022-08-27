from audioop import lin2adpcm
import heapq as heap

L1 = []

heap.heappush(L1,25)
heap.heappush(L1,14)
heap.heappush(L1,2)
heap.heappush(L1,20)
heap.heappush(L1,10)

print(L1)
e = heap.heappop(L1)
print(e)
print(L1)

e = heap.heappushpop(L1,35)  # this function first insert the element and then remove the smallest element
print(e)
print(L1)

e = heap.heapreplace(L1, 1) # this function first remove the smallest elemnt the insert the element

print(e)
print(L1)

print("---------heapify---------")

L2 = [20,14,2,15,10,21]
print(L2)
heap.heapify(L2)  # convert the list into heap
print(L2)

print(heap.nsmallest(3, L2))
print(heap.nlargest(3, L2))