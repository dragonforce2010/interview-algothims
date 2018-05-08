'''Description
Given n items with size Ai, an integer m denotes the size of a backpack. How full you can fill this backpack?

 Notice
You can not divide any item into small pieces.

Have you met this question in a real interview? 
Example
If we have 4 items with size [2, 3, 5, 7], the backpack size is 11, we can select [2, 3, 5], so that the max size we can fill this backpack is 10. If the backpack size is 12. we can select [2, 3, 7] so that we can fulfill the backpack.

You function should return the max size we can fill in the given backpack.

Challenge 
O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.
'''
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size
    # Solution 1
    '''
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [ [False] * (m + 1) for _ in range(n + 1)]
        
        for i in range(0, n + 1):
            dp[i][0] = True
        # for j in range(0, m + 1):
        #     dp[0][j] = False
        
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] 
                if j >= A[i - 1] and dp[i - 1][j - A[i - 1]]:
                    dp[i][j] = True
        
        for j in range(m, -1, -1):
            if dp[n][j]:
                return j
                
        return 0
    '''
        
    # Solution 2
    '''
    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [ [False] * (m + 1) for _ in range(2)]
        
        for i in range(0, n + 1):
            dp[i % 2][0] = True
        
        dp[0][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j] 
                if j >= A[i - 1] and dp[(i - 1) % 2][j - A[i - 1]]:
                    dp[i % 2][j] = True
        
        for j in range(m, -1, -1):
            if dp[n % 2][j]:
                return j
                
        return 0 
    '''
        
        
    # Solution 3
    def backPack(self, m, A):
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans   
'''Summary
State:
f[i][S]: 前i个物品，取出一些是否能够组成和为S，值为true或false

Function：
a[i - 1] 是第i个物品下标，是i - 1
f[i][S] = f[i - 1][S]（不取第i个物品情况） + f[i - 1]S - a[i - 1]

Initialize:
f[i][0] = True
f[0][1.....target] = False

Answer: 
f[n][j] 0<= j <= S, 找最大的

本题中物品的容量，物品的数量都是限制因素，我们可以刚这些因素变量放在dp的小标中表示。dp值可以用布尔值表示
'''

