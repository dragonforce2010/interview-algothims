'''Description
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Given [4, 5, 6, 7, 0, 1, 2] return 0
'''
class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
            
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                start = mid
            else:
                end = mid

        # 注意这里是取最小值        
        return min(nums[start], nums[end])
                
'''Summary
算法武器：基于rotated sorted array的二分法

算法思想：

二分法不仅可以针对单调的序列，还可以针对rotated sorted array进行
本题需要求解在RSA中的最小值，我们把这个最小值定义为第一个小于等于target的元素，target = nums[-1]
二分法擅长解决first index of 或是 last index of 问题
本题需要通过画图了解到我们如何根据mid和target的值更新start和end，事实上这个跟新方式和我们普通的单调的序列相反
当nums[mid] > target， 我们更新的是下届start
其他情况下，我们更新的是上届end
'''