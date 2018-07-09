'''
Find any position of a target number in a sorted array. Return -1 if target does not exist.

Example
Given [1, 2, 2, 4, 5, 5].

For target = 2, return 1 or 2.

For target = 5, return 4 or 5.

For target = 6, return -1.

Challenge
O(logn) time
'''
class Solution:
    def findPosition(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return A[start]

        if A[end] == target:
            return A[end]

        return -1