from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0
        
    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x, v = None):
        u = BinaryTree.Node(x, v)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x : object) -> object:
        # todo
        temp = self.r
        while temp != None:
            if x < temp.x:
                temp = temp.left
            elif x > temp.x:
                temp = temp.right
            else:
                return temp
        return temp
        pass
        
    def find_last(self, x : object) -> BinaryTree.Node:
        # todo
        w = self.r
        prev = None
        while w != None:
            prev = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return prev
        pass

    def find(self, x: object) -> object:
        # todo
        w = self.r
        z = None
        while w != None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return z
        pass
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        # todo
        if p == None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n += 1
        return True
        pass
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def add(self, key : object, value : object) -> bool:
        # todo
        p = self.find_last(key)
        return self.add_child(p, BinaryTree.Node(key, value))
        pass

    def get(self, key : object) -> object:
        # todo
        temp = self.r
        while temp != None:
            if key < temp.x:
                temp = temp.left
            elif key > temp.x:
                temp = temp.right
            else:
                return temp.v
        return None
        pass
    
    def splice(self, u: BinaryTree.Node):
        # todo
        if u.left != None:
            s = u.left
        else:
            s = u.right
        p = None
        if self.r == u:
            self.r = s
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s
        if s != None:
            s.parent = p
        self.n -= 1
        pass 

    def remove_node(self, u : BinaryTree.Node):
        # todo
        if u != None:
            if u.left == None or u.right == None:
                self.splice(u)
            else:
                w = u.right
                while w.left != None:
                    w = w.left
                u.x = w.x
                u.v = w.v
                self.splice(w)
            return u.v
        return None
        pass 

    def remove(self, x : object) -> bool:
        # todo
        if self.find(x) == None:
            raise IndexError
        w = self.find_eq(x)
        return self.remove_node(w)
        pass 
             
    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)


            
