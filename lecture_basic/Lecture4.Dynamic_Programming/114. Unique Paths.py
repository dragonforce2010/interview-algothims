'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Example
Given m = 3 and n = 3, return 6.
Given m = 4 and n = 5, return 35.
'''
class Solution:
    def uniquePaths(self, m, n):
        dp = [ [0] * n for row in range(m)]
        
        for row in range(m):
            dp[row][0] = 1
        for col in range(n):
            dp[0][col] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]