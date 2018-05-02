'''Description
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.
Example
Given [1, 9, 2, 5], the sorted form of it is [1, 2, 5, 9], the maximum gap is between 5 and 9 = 4.
'''
class Solution:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        nums = sorted(nums)
        maxGap = 0
        for i in xrange(1, len(nums)):
            maxGap = max(maxGap, nums[i] - nums[i - 1])
        return maxGap
        

