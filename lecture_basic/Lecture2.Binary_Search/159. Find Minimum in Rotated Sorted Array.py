'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
'''
class Solution:
    def findMin(self, nums):
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        target = nums[-1]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                start = mid
            else:
                end = mid

        # 注意：最后结果返回时我们取最小的那个
        return min(nums[start], nums[end])