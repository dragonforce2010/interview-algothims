'''Description
Given a 2D grid, each cell is either a wall 2, an house 1 or empty 0 (the number zero, one, two), find a place to build a post office so that the sum of the distance from the post office to all the houses is smallest.

Return the smallest sum of distance. Return -1 if it is not possible.
Example
Given a grid:

0 1 0 0 0
1 0 0 2 1
0 1 0 0 0
return 8, You can build at (1,1). (Placing a post office at (1,1), the distance that post office to all the house sum is smallest.)

Challenge 
Solve this problem within O(n^3) time.
'''
class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        
        dist = [[sys.maxint] * n for i in range(m)]
        
        reachable_count = [[0] * n for i in range(m)]
        
        min_dist = sys.maxint
        
        buildings = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, dist, m, n, reachable_count)
                    buildings += 1 
  
        for i in range(m):
            for j in range(n):
                if reachable_count[i][j] == buildings and dist[i][j] < min_dist:
                    min_dist = dist[i][j]
        return min_dist if min_dist != sys.maxint else -1
        
    def bfs(self, grid, i, j, dist, m, n, reachable_count):
        visited = [[False] * n for x in range(m)]
        visited[i][j] = True
        q = collections.deque([(i,j, 0)]) 
        
        while q:
            i, j, l = q.popleft()
            if dist[i][j] == sys.maxint:
                dist[i][j] = 0
            dist[i][j] += l

            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i+x, j+y

                if nx > -1 and nx < m and ny > -1 and ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True 
                    if grid[nx][ny] == 0: 
                        q.append((nx, ny, l+1))
                        reachable_count[nx][ny] += 1 
'''Summary
算法武器：队列 + BFS搜索 + 距离矩阵
算法思路：
- 初始化距离矩阵，dist[i][j] 代表邮局建立在i，j处，所有房子到达此点的最短路径和
- 初始化reachable_count数组，reachable_count[i][j]代表有多少个房子可以走到该点(i,j)
- 遍历全图，寻找房子，计算出房子的总数量，同时计算dist矩阵和出reachable_count矩阵
- 遍历所有点，寻找符合条件的建立邮局位置的点
- 改点需要确保能够可达所有房子，即rechable_count[i][j] = 房子的数量
- 该点是其他房子可达的最短距离点

注意：
- bfs都是从每个房子的角度进行遍历的
- bfs进入队列的元素是一个三元组（i, j, l）,其中i,j代表点的位置，l代表对于点i，j，可以对dist距离矩阵中的dist[i][j]贡献的路径长度值
- bfs每深入一层，这个l就会被累加1
'''