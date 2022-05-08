import tarfile
from requests import NullHandler, head


class _Node:
    __slots__ = '_element','_next','_prev'

    def __init__(self,element,next,prev):
        self._element = element
        self._next = next
        self._prev = prev

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0 

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0 
    
    # add element to the last of doubly linked list
    def addlast(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
            self._tail = newest
        self._size += 1   

    # add element to the beginning of doubly linked list
    def addfirst(self,e):
        newest = _Node(e,None,None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest    
        self._size += 1

    # add element to the beginning of doubly linked list
    def addany(self,e,position):
        newest = _Node(e,None,None)
        p = self._head
        i = 1
        while i < position -1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next._prev = newest
        p._next = newest
        newest._prev = p    
        self._size += 1


    # remove or delete element from the beginning of doubly linked list
    def removefirst(self):
        if self.isempty():
            print('List is empty')
            return 
        e = self._head._element    
        self._head = self._head._next
        self._head._prev = None
        self._size -= 1
        if self.isempty() :
            self._tail = None
        return e    

    # remove or delete element from the beginning of doubly linked list  
    def removelast(self):
        if self.isempty():
            print('List is empty')
            return
        e = self._tail._element
        self._tail = self._tail._prev
        self._tail._next = None
        self._size -= 1
        return e

    # remove or delete element from the beginning of doubly linked list 
    def removeany(self,position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        p._next._prev = p
        self._size -= 1
        return e  

    # display the element of doubly linked list 
    def display(self):
        p = self._head
        while p:
            print(p._element, end= '-->')
            p = p._next
        print()

    # display the element of doubly linked list in reverse order
    def displayrev(self):
        p = self._tail
        while p:
            print(p._element, end= "<--")
            p = p._prev
        print()

L = DoublyLinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)

print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

L.addlast(8)
L.addlast(3)
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

L.addfirst(18)
L.addfirst(30)
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

L.addany(89,3)
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

print(L.removefirst())
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

print(L.removelast())
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()

print(L.removeany(3))
print('Original list')
L.display()
print('List in reverse order')
L.displayrev()