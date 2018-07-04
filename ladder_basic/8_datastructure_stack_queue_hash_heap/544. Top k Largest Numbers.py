'''
Given an integer array, find the top k largest numbers in it.

Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
'''
import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    
    def topk(self, nums, k):
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk
'''
算法武器： heap

构建堆结构，直接调api
堆中元素全局不是有序的，所以得sort一下,然后reverse输出，大数在先
'''