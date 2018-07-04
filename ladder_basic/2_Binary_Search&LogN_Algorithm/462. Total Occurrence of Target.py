'''
Given a target number and an integer array sorted in ascending order. Find the total number of occurrences of target in the array.

Example
Given [1, 3, 3, 4, 5] and target = 3, return 2.

Given [2, 2, 3, 4, 6] and target = 4, return 1.

Given [1, 2, 3, 4, 5] and target = 6, return 0.

Challenge
Time complexity in O(logn)
'''
class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    

    def totalOccurrence(self, A, target):
        if not A:
            return 0
        
        firstIndex = self.findFirstIndexOfTarget(A, target)
        lastIndex = self.findLastIndexOfTarget(A, target)
        
        if firstIndex >= 0 and lastIndex >= 0:
            return lastIndex - firstIndex + 1
        else:
            return 0
            
            
    def findFirstIndexOfTarget(self, A, target):
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
                
        if A[start] == target:
            firstIndex = start
        elif A[end] == target:
            firstIndex = end
        else:
            firstIndex = -1
        
        return firstIndex
        
    def findLastIndexOfTarget(self, A, target):
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] <= target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            lastIndex = end
        elif A[start] == target:
            lastIndex = start
        else:
            lastIndex = -1
        
        return lastIndex