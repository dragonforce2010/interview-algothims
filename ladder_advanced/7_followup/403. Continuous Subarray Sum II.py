'''Description
Given an circular integer array (the next element of the last element is the first element), find a continuous subarray in it, where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number.

If duplicate answers exist, return any of them.
Example
Give [3, 1, -100, -3, 4], return [4,1].
'''
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySumII(self, A):
        if not A:
            return []
        
        sectionsum, maxSum = 0, -sys.maxint
        section = [0, 0]
        start, end = 0, 0
        size, B = len(A), A * 2
        for i in range(len(B) - 1):
            if sectionsum < 0: 
                sectionsum = B[i]
                start = end = i
                
            else:
                sectionsum += B[i]
                end = i
                if len(A) > 1 and end - start > size - 1:
                    sectionsum -= B[start]
                    start += 1
            
            if maxSum < sectionsum:
                maxSum = sectionsum
                section = [start, end % size]
                # if section[1] == 9999:
                #     print(sum(B[0:10000]))
                #     print(sum(B[6794:6783 + size]))
        
            
        return section
        
        
        
    def continuousSubarraySumII2(self, A):        
        sum, maxSum = 0, -sys.maxint
        section = [0, 0]
        start, end = 0, 0
        size, distance = len(A), 0
        for i in xrange(2 * len(A)):
            if start > size - 1:
                break
            
            if distance >= size - 1:
                # if len(A) == 10: print(distance, size)
                sum -= A[start]
                start += 1
                distance -= 1
                
            if sum < 0: 
                sum = A[i % size]
                start = end = i % size
                distance = 0
                
            else:
                sum += A[i % size]
                end = i % size
                distance += 1
            
            if maxSum < sum:
                maxSum = sum
                section = [start, end % size]
        
        return section
        
        
        ans = -0x7fffffff
        sum, total = 0, 0
        start, end = 0, -1
        result = [-1, -1]
        length = len(A)
        for x in A:
            total += x
            if sum < 0:
                sum = x
                start = end + 1
                end = start
            else:
                sum += x
                end += 1
            if sum > ans:
                ans = sum
                result = [start, end]


        start, end = 0, -1
        sum = 0
        for x in A:
            if sum > 0:
                sum = x
                start = end + 1
                end = start
            else:
                sum += x
                end += 1
            if start == 0 and end == length-1:
                continue
            if total - sum > ans:
                ans = total - sum
                result = [(end + 1) % length, (start - 1 + length) % length]

        return result
'''Summary
算法武器：双指针(同向型) + 一次遍历数组

算法思路：
- 本题和I问题的区别在于问题需要对环进行处理
- 环处理的方式有
- 拼接，源串长度变为原来2倍
- 分开讨论，先求连续一段区间的最大值，然后求连续一段区间的最小值，用全局值减去这个最小值作比较

因为题目里面说，是一个环，所以有可能是首尾相连的
第一部分是找没有相连的，也就是直接找最大
第二部分是找相连的，找一段连续的最小值，然后用总的和减去这段最小值，就是首位相连的最大值
'''