'''Description
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

 Notice
0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.
Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
'''
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def __init__(self):
        self.father = []
    
    def numIslands2(self, n, m, operators):
        # Write your code here
        d = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        islandCount, result = 0, []
        for i in xrange(n * m): 
            self.father.append(-1)
        
        for point in operators:
            # map the 2d coordinates to 1d coordinate
            num = point.x * m + point.y
            # if num belongs to no collection, we initialize its collection id to be num
            if self.father[num] == -1:
                islandCount += 1;
                self.father[num] = num
            else:
                result.append(islandCount)
                continue

            # explore 4 directions
            for k in xrange(4):
                x = point.x + d[k][0];
                y = point.y + d[k][1];
                
                if self.check(x, y, n, m):
                    # if union succeeds, we minus the islandCount by 1
                    if self.union(x * m + y, num):
                        islandCount -= 1
      
            result.append(islandCount)

        return result

    # if x and y belong to different collection, we union them and return true
    def union(self, x, y):
        # if x or y doesn't belong to any collection, then we return false
        if self.father[x] == -1 or self.father[y] == -1:
            return False

        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.father[x] = y
            return True
        else:
            return False
    
        
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    # check the boundary
    def check(self, x, y, n, m):
        return x >= 0 and y >=0 and x < n and y < m
'''Summary
算法武器：并查集

本题使用一维的并查集数组self.father 来表示集合，初始化的值为-1，这个-1代表地图上的这个点还没有被探索到。
本题的输入是一系列操作，每一个操作都是对地图的一次探索，每次探索会做一下几件事情：

初始化探索点处的father值，也即更新该点所在的集合id。如果该点此前father/所在集合id为-1，就代表该点被首次探索，我们初始化它的father/集合id为其一维数组的下标，并且将岛屿数量+1，因为我们发现了新大陆
我们沿着该点的四个方向上的周边的点，检查其合法性（不能越界），然后将它们与中心点进行union，因为他们都属于同一father/集合
每进行一次有效合并，我们就将岛屿数量-1，这里声明一下有效合并的定义-合并的两个点隶属于两个不同的集合，然后成功合并为同一个集合，此操称为一次有效合并
注意：本题算法的进行是基于操作序列的，上述的几点是处理一个操作的规则，对于每个操作，我们只更新并查集并且将其周边合并，仅此而已，我们不会像dfs或是bfs那样，要进行递归遍历。

注意：在for循环中，我们检查num位置处的点是否被探索过，如果没有，我们就增加岛屿数，更新并查集，然后将其周边岛屿和其合并到一个集合中
但是，如果该点已经被探索过了，那么我们就没有必要再将其周边岛屿和其合并了，我们仅需把当前的岛屿数量放入结果集中，然后我们continue

时间复杂度分析：
设操作符的规模为k，对于每个操作符，我们仅检查4个方向，所以处理k次操作序列的复杂度是O(4k)
注意：如果不用并查集，而是用普通方法求解此题，时间复杂度就是O(nm*4k), 所以并查集真的是优化了很多
'''    