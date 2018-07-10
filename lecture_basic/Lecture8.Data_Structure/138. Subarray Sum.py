'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''
class Solution:
    def subarraySum(self, A):
        if not A:
            return []

        cache = {}
        presum = 0

        for i in range(len(A)):
            presum += A[i]
            if presum in cache:
                return [presum[sum] + 1, i]
            cache[presum] = i

        return []