'''Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected

Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
'''

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [i for i in range(n + 1)]

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
        # 只有所属不同集合的时候才进行合并
        if roota != rootb:
            # 这里合并的时候，是吧集合rootb合并到集合roota中
            self.father[rootb] = roota

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        return self.find(a) == self.find(b)

'''Summary
算法武器：并查集
'''