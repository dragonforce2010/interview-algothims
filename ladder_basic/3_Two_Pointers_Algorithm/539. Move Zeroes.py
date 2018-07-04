'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example
Given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
'''
class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                if nums[x] != nums[y]:
                    nums[x], nums[y] = nums[y], nums[x]
                y += 1
'''
http://bookshadow.com/weblog/2015/09/19/leetcode-move-zeroes/
解题思路：
题目可以在O(n)时间复杂度内求解

算法步骤：

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0
'''