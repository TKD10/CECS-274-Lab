from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()

    def add(self, x : object):


        """
	    adds an element to the end of this max queue
	    INPUT: x the element to add

        SSLQueue.add(self, x)
        if max_queue is empty
            add x to front no matter what = add_first
        else
            determine the max
            how many items are in max_queue
            if x > max
                create and reassign new list
                add x
            else
                get the tail
                while x > tail
                    remove tail = remove_last
                    get next tail for comparison
                add x last
        """

        SLLQueue.add(self, x)
        if self.max_deque.size() == 0:
            self.max_deque.add(0, x)
        else:
            n = self.max_deque.size()
            max_ele = self.max_deque.get(0)
            if x > max_ele:
                self.max_deque = DLLDeque()
                self.max_deque.add_first(x)
            else:
                tail = self.max_deque.get(n-1)
                while x > tail:
                    r = self.max_deque.remove_last()
                    n -= 1
                    if n == 0:
                        break
                    tail = self.max_deque.get(n-1)
                self.max_deque.add_last(x)



    def remove(self) -> object:

        """
	    removes and returns the element at the head of the max queue


        r = SSLQueue.remove(self, x)
        if we have more items in max_deque
            check if r was equal to max
                remove the head of max_deque
        return r
        """

        r = SLLQueue.remove(self)
        if self.max_deque.size() > 0:
            if r == self.max_deque.get(0):
                self.max_deque.remove(0)
        return r


    def max(self):

        """
	    returns the maximum element stored in the queue
	    """

        return self.max_deque.get(0)


'''
# TESTER
mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
'''