'''
Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.

Return the difference between the sum of the two integers and the target.

Example
Given array nums = [-1, 2, 1, -4], and target = 4.

The minimum difference is 1. (4 - (2 + 1) = 1).

Challenge
Do it in O(nlogn) time complexity.
'''
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return -1
        
        nums.sort()
        l, r = 0, len(nums) - 1
        minDist = sys.maxint
        while l < r:
            value = nums[l] + nums[r]
            dist = abs(target - value)
            if dist < minDist:
                minDist = dist
            if value > target:
                r -= 1
            elif value < target:
                l += 1
            else:
                return 0
                
        return minDist
'''
算法武器：双指针（对冲型）

注意：本题在while体中计算two sum时，我们每次都要计算一次dist，然后更新全局的minDist，然后再更具two sum和taget的比较，我们更新l，r的边界，循环继续进行。

two sum或各种sum的题目，首先排序！重要的事情说三遍
首先排序！
首先排序！
首先排序！
'''