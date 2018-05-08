'''Description
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''
class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        # è·åç©éµçç»´åº¦
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(n): 
            dp[0][i] = matrix[0][i]
        for i in range(1, m): 
            dp[i][0] = matrix[i][0]

        for i in xrange(1, m):
            for j in xrange(1, n): 
                if not matrix[i][j]: 
                    dp[i][j] = 0
                else: 
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
        
        ans = 0
        for i in xrange(m):
            for j in xrange(n): 
                ans = max(ans, dp[i][j])
        
        return ans*ans
'''Summary
算法武器：动态规划
因为动态规划适合求解方案总数，最大最小问题。
'''