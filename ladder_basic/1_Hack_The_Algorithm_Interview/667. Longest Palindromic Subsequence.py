'''Description
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example
Given s = "bbbab" return 4
One possible longest palindromic subsequence is "bbbb".
'''
class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        if not s:
            return 0
            
        n = len(s)
        # dp[i][j]: the longestPalindromeSubseq lenght in subsequence s[i:j+1] 
        dp = [[0] * n for i in range(n)]
        
        # since dp[i][j] needs to use dp[i+1][j] to calculate, so we need to go backwards when looping through
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    
        return dp[0][n - 1]
        