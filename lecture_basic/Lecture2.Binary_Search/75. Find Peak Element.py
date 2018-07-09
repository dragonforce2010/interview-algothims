'''
There is an integer array which has the following features:

The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)

Challenge
Time complexity O(logN)
'''
class Solution:
    def findPeak(self, A):
        if not A or len(A) < 3:
            return 0

        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid

        return end if A[start] < A[end] else start 