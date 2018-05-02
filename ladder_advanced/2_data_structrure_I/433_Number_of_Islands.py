'''Description
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
'''
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        visit = set()
        dirs = [
            (0, 1),
            (0, -1), 
            (1, 0), 
            (-1, 0)
        ]
        
        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in visit:
                    self.dfs(x, y, grid, dirs, visit)
                    count += 1
                        
        return count
        
    
    # 探索点（x, y）以及其周围的四个点
    def dfs(self, x, y, grid, dirs, visit):
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) \
                  and (x, y) not in visit and grid[x][y] == 1:
            visit.add((x, y))
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                self.dfs(nx, ny, grid, dirs, visit)
        

'''Summary
算法武器：深度优先搜索 + 访问数组 + 方向数组
给深度优先搜索一个详细的定义：
- dfs是首先找到它可以计算的所有方向，所有点，然后选择其中一个方向进行验证，如果可行，则访问，然后从访问的那个点起再进行深度优先搜索，直到某个深度走完了，才进行回溯
- 注意dfs是一个递归定义，dfs内部只需要完成对所有可行路径中的每个方向进行一次探索，然后对探索的那个点进行进一步递归调用，一直深入下去
- 因为是深度优先，所以总是在访问某一个点之后就进一步递归调用
- 对于剩下的选择，递归可以进行回溯，所以他们可以被探索到

深度优先搜索的好处：可以不使用任何辅助结构，比如队列，由于其递归调用的特点，天然使用栈，有自动回溯功能
'''