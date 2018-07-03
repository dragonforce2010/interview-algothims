'''
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

Example
For [1, -1, -2, 1], return -3.
'''
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    '''
    题型：求一个数组中的最小子区间和最大子区间问题
    解法：可以使用滚动计算当前位置的presum，实时更新maxpresum 和 minsum的方式求解
    注意：初始化是一个关键，因为我们要求最小区间和，而根据前缀和计算公式：
        minsum = presum - maxpresum
        我们的最小和区间可能是从0开始，所以maxpresum需要初始化为0，才能包含这种情况
        minsum一定是一个子区间，至少包含一个数，所以我们把minsum初始化为nums[0]
        presum初始化为0
    '''
    def minSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
            
        presum, maxsum, minsum = 0, 0, nums[0]
        for num in nums:
            presum += num
            minsum = min(minsum, presum - maxsum)
            maxsum = max(maxsum, presum)
            
        return minsum