'''Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

 Notice
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
'''

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if not edges:
            return True
            
        # 检查边的条数和节点数量的关系
        if len(edges) != n - 1:
            return False
            
        self.father = [i for in range(n + 1)]
        
        for n1, n2 in edges:
            root1 = self.find(n1)
            root2 = self.find(n2)
            if root1 == root2:
                return False
            else:
                # 一边读取边的信息，一边根据读入的信息更新当前的并查集
                self.father[root2] = self.father[root1] 
                
        return True
        
        
    def find(self, x):
        if self.father[x] == x:
            return x
            
        self.father[x] = self.find(self.father[x])
        return self.father[x]

'''Summary
算法武器：并查集

注意：
- 有效的树的判定条件是树中不存在环
- 如果两个节点有相同的父亲，同时这两个点又直接相连，那么就构成环了
- n个节点构成的树有n-1条边，如果这个不相等，则一定不是树
- 在没有环的情况下，同时n各点又有n-1条边，那么这就一定是树了。
算法武器2：BFS
本题还可以用BFS求解，用于判断联通性，因为树一定是联通的，而图有可能不连通，所以用BFS可以做判断。

1.树
首先，我们得了解一下树。树，这种数据结构每个节点有零个或多个子节点；没有父节点的节点称为根节点；每一个非根节点有且只有一个父节点，所以树有一个关键的性质就是n个结点的树有n-1条边。假如题中的边数不是n-1，那么一定不是树。
2.判断完边后
判断完边数之后，这里还需要再思考一个问题，有n-1条边的图一定是树吗？答案是否定的，因为题中并没有说给我们的一定是一个连通图，也就是说，很有可能给我们的图是几个图，所以我们判断完边数之后还得判断是否是一个连通图。
3.判断是否为连通图
那么现在问题就变成了判断是否为一个连通图，判断连通图的方法在参考程序里给了两种方法，一种是从一个点出发，判断与这个点相连的点数是否等于n(如果不是联通的，那visit就不等于n)，第二种就是用并查集的方法判断是否联通。
'''