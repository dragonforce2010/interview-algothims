'''
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Example
For L=[232, 124, 456], k=7, return 114.

Challenge
O(n log Len), where Len is the longest length of the wood.
'''
class Solution:
    def woodCut(self, L, k):
        if not L or k < 0:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.calculatePieces(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.calculatePieces(L, end) >= k:
            return end

        if self.calculatePieces(L, start) >= k:
            return start

        return 0
            

    def calculatePieces(self, L, pieceLenght):
        if not L:
            return 0

        return sum(map(lambda x: x // pieceLenght, L))
