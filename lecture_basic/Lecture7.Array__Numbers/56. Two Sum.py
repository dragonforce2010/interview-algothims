'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''
class Solution:
    def twoSum(self, nums, target):
        cache = {}
        for i in range(len(nums)):
            if target - num[i] in cache:
                return [cache[target - num[i]] + 1, i + 1]
            cache[nums[i]] = i

        return [-1, -1]
