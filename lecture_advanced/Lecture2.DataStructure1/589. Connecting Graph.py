'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), add an edge to connect node a and node b`.
query(a, b), check if two nodes are connected
Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
'''
class ConnectingGraph:
    def __init__(self, n):
        self.father = [ i for i in range(n + 1)]

    def find(self, x):
        if self.father[x] == x:
            return x

        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self, a, b):
        fathera = self.find(a)
        fatherb = self.find(b)
        if fathera != fatherb:
            self.father[fatherb] = fathera

    def query(self, a, b):
        return self.find(a) == self.find(b)

'''
算法武器：并查集
'''
