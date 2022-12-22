import numpy as np
import random
from ArrayQueue import ArrayQueue

class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)
            

    def remove(self) -> np.object :
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        # generating a random position in our queue to remove, 0, n-1
        # assuming that r = translate random number (say r) from position in queue to index of array
        # swap the values stored at a[j] and a[r]; r is now at the front of our queue
        # return super().remove()
        if self.n == 0:
            raise IndexError()
        i = random.randint(0, self.n - 1)
        self.a[self.j % len(self.a)], self.a[(self.j + i) % len(self.a)] = \
            self.a[(self.j + i) % len(self.a)], self.a[self.j % len(self.a)]
        return super().remove()

     




