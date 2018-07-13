'''
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?
'''
class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return -sys.maxsize

        maxSum, minPreSum, presum = nums[0], 0, 0
        for num in nums:
            presum += num
            maxSum = max(maxSum, presum - minPreSum)
            minPreSum = min(minPreSum, presum)

        return maxSum