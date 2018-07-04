'''
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
'''
class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        
        count = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            value = nums[l] + nums[r]
            if value > target:
                r -= 1
            elif value < target:
                l += 1
            else:
                l += 1
                r -= 1
                count += 1
                while l < r and nums[l] == nums[l - 1]: l += 1
                while l < r and nums[r] == nums[r + 1]: r -= 1
        
        return count

'''
算法武器：双指针

本题要求解的是unique pairs，所以我们需要加入去重操作。
去重操作过程：

使用while循环，进行去重，while循环的条件和外层的while循环条件相同
去重只在得到答案部分进行去重，因为我们只希望避免重复的答案。当然在前面的两个条件中去重也没有问题
'''