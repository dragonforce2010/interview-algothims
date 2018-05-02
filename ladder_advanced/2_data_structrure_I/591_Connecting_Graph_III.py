'''Description
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:
1. connect(a, b), an edge to connect node a and node b
2. query(), Returns the number of connected component in the graph
Example
5 // n = 5
query() return 5
connect(1, 2)
query() return 4
connect(2, 4)
query() return 3
connect(1, 4)
query() return 3

'''
class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [i for i in range(n + 1)]
        self.count = n


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
            self.count -= 1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count

'''Summary
算法武器：并查集 + 成员变量count（维护联通块的个数）
注意：
- connect方法在调用时，只有在root_a != root_b的情况下才进行合并，才会修改self.count。
'''