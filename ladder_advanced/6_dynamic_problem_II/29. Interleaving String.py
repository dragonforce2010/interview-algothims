'''Description
Given three strings: s1, s2, s3, determine whether s3 is formed by the interleaving of s1 and s2.

Have you met this question in a real interview? 
Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
Challenge 
O(n2) time or better
'''
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    # When you see string problem that is about subsequence or matching, dynamic programming method should come to your mind naturally.
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1] and dp[i - 1][0]:
                dp[i][0] = True
        
        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1] and dp[0][j-1]:
                dp[0][j] = True
        
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                c = s3[i + j - 1]
                if c == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                
                if c == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[len(s1)][len(s2)]
'''Summary
http://www.cnblogs.com/springfor/p/3896159.html
'''