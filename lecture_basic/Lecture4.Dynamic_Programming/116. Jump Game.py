'''
116. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution:
    def canJump(self, A):
        if not A:
            return False

        dp = [False] * len(A)
        dp = True

        # dp[i]状态的计算是使用dp[0 ~ i - 1]的状态来联合计算的，而不是仅仅靠dp[i-i]
        # 只要在0 ~ i - 1个状态中，我们能找到一个状态自己本身可达，同时又能够可达i，那么我们认为dp[i]可达
        for i in range(1, len(A)):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break

        return dp[len(A) - 1]