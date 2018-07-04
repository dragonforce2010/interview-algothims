'''
Given an integer array, sort it in ascending order. Use quick sort, merge sort, heap sort or any O(nlogn) algorithm.

Example
Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5].
'''
import random
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        self.qsort(A, 0, len(A) - 1)
    
    
    # inplace quick sort
    def qsort(self, A, start, end):
        if start >= end: 
            return
    
        i, j = start, end
        # 随机选择一个数轴记录
        pivot = A[random.randint(start, end)]
        
        
        while i < j:
            while A[i] < pivot: 
                i += 1
            while A[j] > pivot: 
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j - 1
        A[i - 1] = pivot
        
        self.qsort(A, start, i - 2)
        self.qsort(A, i, end)