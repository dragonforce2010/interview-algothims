'''
Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.
'''
class Solution:
    def recoverRotateSortedArray(self, nums):
        if len(nums) < 2:
            return nums

        for index in range(len(nums) - 1):
            if nums[index] > nums[index + 1]:
                self.reverse(nums, 0, index)
                self.reverse(nums, index + 1, len(nums) - 1)
                self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        if len(nums) < 2:
            return nums

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1