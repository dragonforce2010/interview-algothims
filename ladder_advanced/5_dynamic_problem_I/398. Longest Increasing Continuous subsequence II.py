'''Description
Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).
Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25

Challenge 
O(nm) time and memory.
'''
class Solution:
    DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    # @param {int[][]} A an integer matrix
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequenceII(self, A):
        if len(A) == 0 or len(A[0]) == 0:
            return 0
            
        self.n = len(A)
        self.m = len(A[0])
        self.matrix = [[0] * self.m for i in xrange(self.n)]
        
        for i in xrange(self.n):
            for j in xrange(self.m):
                self.search(A, i, j)
        
        return max(max(row) for row in self.matrix)
        
    def search(self, A, x, y):
        if self.matrix[x][y] != 0:
            return self.matrix[x][y]
        
        longest = 1
        for dx, dy in self.DIRECTIONS:
            if x + dx < 0 or x + dx >= self.n:
                continue
            if y + dy < 0 or y + dy >= self.m:
                continue
            if A[x][y] >= A[x + dx][y + dy]:
                continue
            longest = max(longest, self.search(A, x + dx, y + dy) + 1)
        self.matrix[x][y] = longest
        return self.matrix[x][y]
        