from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.x = x
            
    def __init__(self) :
        self.head = None
        self.tail = None
        self.n = 0
   
    def push(self, x : np.object) :
       # todo
       # create a new node storing x
       new_node = self.Node(x)
       # assign new node.next to head
       new_node.next = self.head
       # assign head the new node
       self.head = new_node
       # increment n by 1
       self.n += 1
       # If n=1 new node is also tail
       if self.n == 1:
           self.tail = new_node

        
    def pop(self) -> np.object:
        # todo
        # check the precondition, if n = 0 return None
        if self.n == 0:
            raise IndexError()
        # create temp var for head.x
        temp = self.head.x
        # head.next = head
        self.head = self.head.next
        # decrement by 1
        self.n -= 1
        # check invariant, if n = 0, tail = None
        if self.n == 0:
            self.tail = None
        # return temp
        return temp


    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x




