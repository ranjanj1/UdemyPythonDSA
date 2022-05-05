from numpy import disp


class _Node:
    __slots__ = '_element','_next'
    
    def __init__(self,element,next):
        self._element = element
        self._next = next

class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0 

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0
    # add element to the last of circular linked list
    def addlast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    # mentod to display the circular linked list
    def display(self):
        p = self._head
        i = 0
        while i < len(self):
            print(p._element, end=' --> ')
            p = p._next
            i += 1
        print()    


C = CircularLinkedList()
C.addlast(3)
C.addlast(5)
C.addlast(7)
C.addlast(4)

C.display()
print('Size:', len(C))
C.addlast(7)
C.addlast(4)
C.display()


