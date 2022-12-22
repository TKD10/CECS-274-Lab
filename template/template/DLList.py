from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        # todo
        if i < 0 or i > self.n:
            return IndexError()
        if i < self.n/2:
            p = self.dummy.next
            j = 0
            while j < i:
                j += 1
                p = p.next
        else:
            p = self.dummy
            j = self.n
            while j > i:
                j -= 1
                p = p.prev
        return p

        
    def get(self, i) -> np.object:
        # todo
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.get_node(i).x


    def set(self, i : int, x : np.object) -> np.object:
        # todo
        if i < 0 or i >= self.n:
            raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

        pass 

    def add_before(self, w : Node, x : np.object) -> Node:
        # todo
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1

        if self.n == 1:
            self.dummy.next = u
            self.dummy.prev = u
        return u

            
    def add(self, i : int, x : np.object)  :
        # todo
        if i < 0 or i > self.n:
            raise IndexError()
        self.add_before(self.get_node(i), x)


    def _remove(self, w : Node) :
       # todo
       if self.n == 0:
           raise IndexError()
       w.prev.next = w.next
       w.next.prev = w.prev
       self.n -= 1

       if self.n == 0:
           self.dummy.prev = self.dummy
           self.dummy.next = self.dummy
       return w.x

    
    def remove(self, i :int) :
        if i < 0 or i > self.n:  raise IndexError()
        return self._remove(self.get_node(i))

    def reverse(self):
        # reverse the list itself
        '''
                    dummy -> next = head
                    dummy -> prev = tail
        where is head
        where is tail
        define a curr pointer
        stop when we hit dummy
            temp = c.next
            c.next = c.previous
            c.previous = temp
            curr = temp
            point current to next node
        take care of dummy

        '''
        head = self.dummy.next
        tail = self.dummy.prev

        prev = self.dummy
        curr = self.dummy.next
        curr_next = curr.next
        while curr is not self.dummy:
            curr.next = prev
            curr.prev = curr_next

            prev = curr
            curr = curr_next
            curr_next = curr_next.next

        self.dummy.next = tail
        self.dummy.prev = head


    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        # todo
        # for(size//2)
        # [a v a]
        # [h a n n a h] f stands for front and b stands for back
        #  f         b
        #    f     b
        #      f b

        # use get to compare front and back and make sure they are equal, then decrement each time
        n = self.dummy.next
        p = self.dummy.prev
        while n.x == p.x and n != self.dummy:
            n = n.next
            p = p.prev
        return n == self.dummy


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x
