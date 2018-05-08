'''Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
Example
Given [3, 8, 4], return 8.

Challenge 
O(n) time and O(1) memory.
'''
class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
            
        dp = [0] * (len(A) + 1)
        dp[0], dp[1] = 0, A[0]
        
        for i in range(2, len(A) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + A[i - 1])
            
        return dp[len(A)]
'''Summary
算法武器：动态规划

本题属于序列型动态规划，不是坐标型动态规划，所以dp[i]或者f[i]定义为：robber前i个房子能够获取的最大金钱。答案表达式为dp[n]或f[n]
'''