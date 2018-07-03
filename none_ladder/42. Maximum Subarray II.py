'''
Given an array of integers, find two non-overlapping subarrays which have the largest sum.
The number in each subarray should be contiguous.
Return the largest sum.

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have the largest sum 7.

Challenge
Can you do it in time complexity O(n) ?
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    '''
    使用拆分的思想，将大问题划分为子问题，然后逐步求解
    1.题目中涉及到了拆分，那么我就可以穷举出所有的拆分点
    2.对于拆分的每一部分，我们可以将其看成一个求给定子数组的最大区间和的问题
      这样整个问题就变成：maxsum = leftmaxsum + rightmaxsum
    '''
    def maxTwoSubArrays(self, nums):
        # write your code here
        if not nums:
            raise Exception("Input nums can not be None or Empty!")
            
        maxsum = -789876556778
        for splitIndex in range(len(nums) - 1):
            leftMaxSum = self.maxSubArraySum(nums, 0, splitIndex)
            rightMaxSum = self.maxSubArraySum(nums, splitIndex + 1, len(nums) - 1)
            maxsum = max(maxsum, leftMaxSum + rightMaxSum)
            
        return maxsum
        
    
    def maxSubArraySum(self, nums, start, end):
        if not nums:
            return 0
            
        # 注意初始化，初值很重要    
        presum, maxsum, minPresum = 0, nums[start], 0
        for i in range(start, end + 1):
            presum += nums[i]
            maxsum = max(maxsum, presum - minPresum)
            minPresum = min(minPresum, presum)
            
        return maxsum