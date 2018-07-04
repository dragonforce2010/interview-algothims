'''
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Example
Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
'''
class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    # def twoSum5(self, nums, target):
    #     # Write your code here
    #     if not nums:
    #         return 0
            
    #     i, j, count = 0, len(nums) - 1, 0
    #     nums.sort()
    #     while i < j:
    #         if nums[i] + nums[j] > target:
    #             j -= 1
    #         else:
    #             count += j - i
    #             i += 1
        
    #     return count
        
        
    def twoSum5(self, nums, target):
        if not nums:
            return 0
            
        left, right, count = 0, len(nums) - 1, 0
        nums.sort()
        
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                count += right - left
                left += 1
        
        return count
'''
算法武器：双指针

Two sum问题，使用双指针（对冲型/相向型）方法，对原数组进行排序，然后根据左右两个指针所指向元素的和与target的关系对左右指针进行调节同时进行个数统计。
'''