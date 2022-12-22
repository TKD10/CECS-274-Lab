from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        # todo
        self.adj[i][j] = 1

    def remove_edge(self, i : int, j : int):
        # todo
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        # todo
        return self.adj[i][j] == 1

    def out_edges(self, i) -> List:
        # todo
        out = ArrayList.ArrayList()
        for k in range(len(self.adj[i])):
            if self.adj[i][k] == 1:
                out.append(k)
        return out


    def in_edges(self, i) -> List:
        # todo
        in_ed = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k, i):
                in_ed.append(k)
        return in_ed

    def bfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        visited = np.zeros(self.n)
        queue = ArrayQueue.ArrayQueue()

        traversal.append(r)
        visited[r] = 1
        queue.add(r)
        while queue.size() > 0:
            cur = queue.remove()
            neighbors = self.out_edges(cur)
            for i in range(neighbors.size()):
                neighbor = neighbors.get(i)
                if visited[neighbor] == 0:
                    traversal.append(neighbor)
                    visited[neighbor] = 1
                    queue.add(neighbor)
        return traversal

    def dfs(self, r : int):
        # todo
        traversal = ArrayList.ArrayList()
        visited = np.zeros(self.n, dtype=int)
        stack = ArrayStack.ArrayStack()
        stack.push(r)
        while stack.size() > 0:
            cur = stack.pop()
            if visited[cur] == 0:
                traversal.append(cur)
                visited[cur] = 1
            neighbors = self.out_edges(cur)
            for i in reversed(range(neighbors.size())):
                neighbor = neighbors.get(i)
                if visited[neighbor] == 0:
                    stack.push(neighbor)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s


# g = AdjacencyMatrix(6)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(0, 3)
# g.add_edge(2, 4)
# g.add_edge(4, 5)
# g.add_edge(1, 4)
# g.add_edge(4, 5)

# print(g)
# print(g.bfs(0))

g = AdjacencyMatrix(12)
g.add_edge(0, 1)
g.add_edge(0, 9)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(1, 10)
g.add_edge(1, 11)
g.add_edge(2, 1)
g.add_edge(2, 3)
g.add_edge(2, 11)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 3)
g.add_edge(4, 5)
g.add_edge(4, 11)
g.add_edge(5, 4)
g.add_edge(5, 6)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(6, 11)
g.add_edge(7, 6)
g.add_edge(7, 8)
g.add_edge(7, 10)
g.add_edge(8, 7)
g.add_edge(8, 9)
g.add_edge(9, 0)
g.add_edge(9, 8)
g.add_edge(9, 10)
g.add_edge(10, 1)
g.add_edge(10, 7)
g.add_edge(10, 9)
g.add_edge(10, 11)
g.add_edge(11, 2)
g.add_edge(11, 4)
g.add_edge(11, 6)
g.add_edge(11, 10)

print(g)
print("BFS(0):", g.bfs(0))
print("Expected: [0, 1, 9, 2, 10, 11, 8, 3, 7, 4, 6, 5]")
print("\nDFS(0):", g.dfs(0))
print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")


