'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
'''
class Solution:
    '''
    (1) Maxmum
    (2) Minmum
    (3) Total number of solutions
    (4) Feasible or not
    
    1. Definition
        - dp[i][j]: The minmum path sum from (0,0) to (i, j)
    2. Answer
        - dp[m - 1][n - 1]
    3. State transfer equation
        - dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        - Note: You can only move either down or right at any point in time.
    4. Initialization
        - dp[i][0]: dp[i - 1][0] + grid[i][0]
        - dp[0][j]: dp[0][j - 1] + grid[0][j]
    '''
    def minPathSum(self, grid):
        if not grid:
            return -1

        m, n = len(grid), len(grid[0])
        dp = [ [0] * n for row in range(m)]

        for row in range(m):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
        for col in range(n):
            dp[0][col] = dp[0][col - 1] + grid[0][col - 1]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]

        return dp[m - 1][n - 1]