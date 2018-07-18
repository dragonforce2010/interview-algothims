'''
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
return 3
'''
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count, visited = 0, set()
        self.dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        for i in range(m):
            for j in range(n):
                if self.check(grid, i, j, visited):
                    self.dfs(grid, i, j, visited)
                    count += 1

        return count

    def check(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] and (i, j) not in visited:
            return True
        
        return False

    def dfs(self, grid, x, y, visited):
        visited.add((x, y))
        for dx, dy in self.dirs:
            nx = x + dx
            ny = y + dy
            if self.check(grid, nx, ny, visited):
                visited.add((nx, ny))
                self.dfs(grid, nx, ny, visited)

'''
算法武器：深度优先搜索 + 访问数组 + 方向数组

给深度优先搜索一个详细的定义：

dfs是首先找到它可以计算的所有方向，所有点，然后选择其中一个方向进行验证，如果可行，则访问，然后从访问的那个点起再进行深度优先搜索，直到某个深度走完了，才进行回溯
注意dfs是一个递归定义，dfs内部只需要完成对所有可行路径中的每个方向进行一次探索，然后对探索的那个点进行进一步递归调用，一直深入下去
因为是深度优先，所以总是在访问某一个点之后就进一步递归调用
对于剩下的选择，递归可以进行回溯，所以他们可以被探索到
深度优先搜索的好处：可以不使用任何辅助结构，比如队列，由于其递归调用的特点，天然使用栈，有自动回溯功能
'''