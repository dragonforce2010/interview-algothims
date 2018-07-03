'''
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?
'''
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    '''
    题型：求一个数组中的最小子区间和最大子区间问题
    解法：可以使用滚动计算当前位置的presum，实时更新maxsum和 minPresum的方式求解
    注意：初始化是一个关键，因为我们要求最小区间和，而根据前缀和计算公式：
        maxsum = presum - minPresum
        我们的最大和区间可能是从0开始，所以minPresum需要初始化为0，才能包含这种情况
        maxsum一定是一个子区间，至少包含一个数，所以我们把maxsum初始化为nums[0]
        presum初始化为0
    '''
    '''
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            raise Exception("Input nums can not be None or Empty!")
            
        presum, maxsum, minPresum = 0, nums[0], 0
        for num in nums:
            presum += num
            maxsum = max(maxsum, presum - minPresum)
            minPresum = min(minPresum, presum)
            
        return maxsum
            
        
