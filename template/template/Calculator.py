import numpy as np
import ArrayStack
# import BinaryTree
# import ChainedHashTable
# import DLList
# import operator

class Calculator:
    def __init__(self) :
        self.dict = None  # ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)
        
    def matched_expression(self, s : str) -> bool :
        # todo
        # s -> '3+4*(2/3) + (5*10)'
        # cannot count stack because ')(3+4)('
        # '()()('
        # hint is to use ArrayStack
        stack = ArrayStack.ArrayStack()
        for w in s:
            if w == "(":
                stack.push(w)
            if w == ")":
                if stack.size() > 0:
                    stack.pop()
                else:
                    return False
        return stack.size() == 0
        # stack.push(x)  actual code to use
        # stack.pop()    actual code to use
        # stack.size() ==   actual code to use
        # for char in s:  #takes all the elements/characters in the string
            # check for a parenthesis
            # if try to pop on an empty stack it will give an index error
            # return False actual code to use
        # cannot just return true at the end of the for loop
        # check size of our stack



    def build_parse_tree(self, exp : str) ->str:
        # todo
        pass 

    def _evaluate(self, root):
        op = { '+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        # todo
        pass 

    def evaluate(self, exp):
        parseTree = self.build_parse_tree(exp)
        return self._evaluate(parseTree.r)
        
        
