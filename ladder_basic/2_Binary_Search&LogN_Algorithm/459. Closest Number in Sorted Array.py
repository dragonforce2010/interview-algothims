'''
Given a target number and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

Example
Given [1, 2, 3] and target = 2, return 1.

Given [1, 4, 6] and target = 3, return 1.

Given [1, 4, 6] and target = 5, return 1 or 2.

Given [1, 3, 3, 4] and target = 2, return 0 or 1 or 2.

Challenge
O(logn) time complexity.
'''
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    
    def closestNumber(self, A, target):
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
                
        return start if abs(A[start] - target) < abs(A[end] - target) else end
'''Summary
算法武器：二分法（前提数组排序）

使用二分法尝试查找给定target的位置，如果找到就返回，如果没有找到就返回两个端点start，end中离target比较近的那个。

注意本题的二分法模板（如果没有找到target元素）会最终确定一个start和end边界使得元素的值介于start和end之间

'''