'''
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)
'''
class Solution:
    '''
    1.Definition
        - dp[i]: jump from index 0 to i, the length of longest LIS
        - Note: the end of LIS is num[i]
    2.Answer
        - max(dp): longest LIS could end with any index, so we use max to get the longest LIS length 
    3.State transfer equation
        - for index i, if num[j] < num[i] then dp[i] = max(dp[j] + 1, dp[i])
    4.Initialization
        - dp[i] = 1
    '''
    def longestIncreasingSubsequence(self, nums):
        if not nusm:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

'''
算法武器： 动规

dp[i]定义：数组以i位置处的nums[i]作为最大值的区间的最长递增子序列长度

这是一道经典的使用中间状态dp[j]求解dp[i], 而不是使用前一个状态dp[i-1]
状态转移方程描述的是dp[i] 和 中间状态dp[j]的状态变迁

注意：本题是subsequence，是讲顺序的，所以我们不能给数组排序
'''