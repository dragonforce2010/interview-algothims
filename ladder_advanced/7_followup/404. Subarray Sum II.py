'''Description
Given an integer array, find a subarray where the sum of numbers is in a given interval. Your code should return the number of possible answers. (The element in the array should be positive)
Example
Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

[0, 0]
[0, 1]
[1, 1]
[2, 2]
'''
class Solution:
    # @param {int[]} A an integer array
    # @param {int} start an integer
    # @param {int} end an integer
    # @return {int} the number of possible answer
    def subarraySumII(self, A, start, end):
        # Write your code here
        size = len(A)
        sums = [0] * (size + 1)
        for i in range(size):
            # in python sums[-1] is the last elem of the array
            # when i = 0, sums[i - 1] = sums[-1] = 0
            sums[i] = sums[i - 1] + A[i]
        
        result = 0
        for i in range(size):
            # bisect left
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] < start:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == size: break
            left = lo
            
            # bisect right
            lo, hi = i, size
            while lo < hi:
                mid = (lo + hi) // 2
                if sums[mid] - sums[i - 1] > end:
                    hi = mid
                else:
                    lo = mid + 1
            if lo == i and A[i] > size:
                continue
            right = lo
                  
            result += right - left
            
        return result
        
        # Solution2: It's working but got time out issue
        # size = len(A)
        # sums = [0] * (size + 1)
        # for i in range(size):
        #     sums[i] = sums[i - 1] + A[i]
            
        # result = 0
        # for i in range(size):
        #     for j in range(i, size):
        #         if start <= sums[j] - sums[i - 1] <= end:
        #             result += 1 
        
        # return result
'''Summary
算法武器：数组前缀和 + 子区间和 + 二分法 + 前缀和有序性原理

因为都是整数，所以数组的前缀和自身是有序的，我们可以使用二分法进行查找，找到一个左边界，找到一个右边界，然后这两个边界只差就是答案。即

result = right - left
因为题目要求子段和在区间 [start, end] 之间，注意此时的A数组已经发生变化，A[i]记录的是前i个数的前缀和。那么任何一个子段和即使两个前缀值的差，假设我们让A[i]作为被减数，也就是说start <= A[i] - value <= end
得出 value <= A[i] - start 且 A[i] - end <= value
find(A, len, r+1) 就是找出 value <= A[i] - start 这个条件满足要求的。
find(A, len, l) 就是找出 A[i] - end <= value 不满足这个要求的，相减就是剩下满足要求的value的个数。
'''