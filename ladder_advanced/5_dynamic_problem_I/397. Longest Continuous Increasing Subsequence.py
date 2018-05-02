'''Description
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
'''
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # need to check both directions according by the problem description
        return max(self.getLongest(A), self.getLongest(list(reversed(A))))
    
    # find the LICS in Array A    
    def getLongest(self, A):
        length, longest = 0, 0
        for index, _ in enumerate(A):
            # check if we need to reset length
            if index == 0 or A[index] < A[index - 1]:
                length = 1
            else:
                length += 1
            # keep the record of the longest    
            longest = max(longest, length)
        return longest
'''Summary
注意：题目中要求的是下标连续的子序列，我刚开始错把它看成下标可以不连续，lol
题目基本框架：
扫描数组，根据条件重置局部解，并且不断更新全局解。
问题复杂度为O（n）

对比题目：
http://lintcode.com/en/problem/continuous-subarray-sum/
求具有最大和的连续子数组的题目中我们也使用了这个策略，一次扫描，局部解的计算和重置以及全局解的更新。只不过那道题更复杂一点，还需要使用前向型双指针策略
'''