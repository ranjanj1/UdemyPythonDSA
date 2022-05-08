class _Node:
    __slots__ = '_element', '_next'
    def __init__(self,element,next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    # to calculate the length of linked list 
    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    # to add element at the end of the linked list
    def addlast(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest 
        
        self._tail = newest      
        self._size  += 1

    # add element at the beginning of the linked list
    def addfirst(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest    
        self._size += 1


    # to add element anywhere in the linked list
    def addany(self,e,position):
        newest = _Node(e,None)
        p = self._head
        i = 1
        while i < position -1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1


    # to search element in the linked list
    def search(self,key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1        

    # remove or delete the element from the beginning of the linked list
    def removefirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.isempty():
            self._tail = None 
        return e    

    #remove or delete the last element of the linked list
    def removelast(self):
        if self.isempty():
            print("List is empty")
            return 
        p = self._head
        i = 1
        while i < len(self) -1:
            p = p._next
            i += 1
        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1
        return e

    #remove or delete element at any position
    def removeany(self,position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e

    # to display the elemnet of linked list
    def display(self):
        p = self._head
        while p:
            print(p._element, end=' --> ')  # end here is used to sepereate one elemnet with other
            p = p._next
        print()    


L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)

L.display()
print('size:', len(L))

L.addlast(8)
L.addlast(3)
L.display()
print('size:', len(L))

print("Result:", L.search(3))

L.addfirst(0)
L.display()

L.addany(11,1)
L.display()

print(L.removefirst())
L.display()

print(L.removelast())
L.display()

print(L.removeany(3))
L.display()


