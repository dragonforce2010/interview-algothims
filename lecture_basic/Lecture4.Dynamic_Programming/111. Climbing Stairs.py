'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
'''
class Solution:
    '''
    1. Definition
        - dp[i]: how many distinct ways to jump to step i
    2. Answer
        - dp[n]
    3. State transfer equation
        - dp[i] = dp[i - 1] + dp[i - 2]
    4. Initialization
        - dp[0] = 1
        - dp[1] = 1
    '''
    def climbStairs(self, n):
        if n == 0:
            return 0

        if n in [1, 2]:
            return n

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
'''
算法武器：动态规划dp

因为是求方案数，所以第一时间想到dp
本题使用的是序列型的动态规划，所以我们的dp[i]代表跳完前i个台阶的方案数。我们的答案是dp[n],即跳完前n个台阶的方案数
'''