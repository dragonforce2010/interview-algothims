'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume NO duplicates in the array.

Example
[1,3,5,6], 5 → 2

[1,3,5,6], 2 → 1

[1,3,5,6], 7 → 4

[1,3,5,6], 0 → 0

Challenge
O(log(n)) time
'''
class Solution:
    def searchInsert(self, A, target):
        if not A or A[0] >= target:
            return 0

        if A[-1] < target:
            return len(A)

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        if A[start] >= target:
            return start

        return end
