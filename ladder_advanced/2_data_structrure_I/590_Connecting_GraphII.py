'''Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(a), Returns the number of connected component nodes which include node a.
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
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        
    def find(self, x):
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        roota = self.find(a)
        rootb = self.find(b)
        if roota != rootb:
            self.father[rootb] = roota
            self.size[roota] += self.size[rootb]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        roota = self.find(a)
        return self.size[roota]


'''Summary
算法武器：并查集 + size数组
'''
