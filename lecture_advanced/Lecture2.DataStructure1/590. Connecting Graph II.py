'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(a), Returns the number of connected component nodes which include node a.
Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3
'''
class ConnectingGraph2:
    def __init__(self, n):
        self.father = [i for i in range(n + 1)]
        self.size = [1 for _in range(n + 1)]

    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(father[x])
        return self.father[x]

    def connect(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota != rootb:
            self.father[rootb] = roota
            self.size[roota] += self.size[rootb]

    def query(self, a):
        roota = self.find(a)
        return self.size[roota]

'''
算法武器：并查集 + size数组
'''