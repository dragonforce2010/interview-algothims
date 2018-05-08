'''Description
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

 Notice
You couldn't cut wood into float length.

If you couldn't get >= k pieces, return 0.
Example
For L=[232, 124, 456], k=7, return 114.

Challenge 
O(n log Len), where Len is the longest length of the wood.
'''
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        
        if not L:
            return 0
        
        if k <= 0:
            return 0
            
        start, end = 0, max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            if sum(map(lambda x : x / mid, L)) >= k:
                start = mid
            else: 
                end = mid
                
        if sum(map(lambda x : x / end, L)) >= k:
            return end
        else:
            return start
'''Summary
算法武器：二分法

算法思想：
- 本题二分是答案
- 我们需要求出最长的长度，那么我就尝试二分这个长度，要做到这点，我们需要知道这个长度的上届和下届，然后我们进行二分，根据条件判断我们是需要增加长度还是减少长度
- 对于每一个二分的长度，我们查看按照这种长度切分的块数是否满足大于等于k的条件，如果满足，那么我们可以尝试加大这个length，如果不可以，我们尝试减小这个length

本题还和一个简单算法思想相关-枚举法：
即对于需要求解的答案，我们尝试所有的可能性，对其进行计算

本题首先想到枚举法，然后使用二分法进行优化，这个是一个思维过程。
'''