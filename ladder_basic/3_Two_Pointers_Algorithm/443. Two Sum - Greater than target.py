'''
Given an array of integers, find how many pairs in the array such that their sum is bigger than a specific target number. Please return the number of pairs.

Example
Given numbers = [2, 7, 11, 15], target = 24. Return 1. (11 + 15 is the only pair)

Challenge
Do it in O(1) extra space and O(nlogn) time.
'''
class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        if not nums:
            return 0
        
        nums.sort()
        count, i, j = 0, 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] <= target:
                i += 1
            else:
                count += j - i
                j -= 1
        
        return count
'''
算法武器：排序 + 双指针

算法思路：

排序
定义双指针left，right分别指向最左和最右
在while循环中，计算2sum，即left指针和right指针之和，并将其和target作比较
如果小于等于target，那么我们就调整下届，将i指针+1
如果大于target，那么只是我们解的情形，我们找到了一对(i, j)是的满足题目要求，同时我们也知道(i + 1, j), (i + 2, j)....(j - 1, j)都是满足和大于target的情形，所以对于当前的j，总共的有效解的个数为j - i,我们把这个数目累加到count标量，最后将j变量更新 -1
'''