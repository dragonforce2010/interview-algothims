'''Description
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.
Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Challenge 
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
'''
class Solution:
    #@param A: An list of list integer 
    #@return: The index of position is a list of integer, for example [2,2]
    def findPeakII(self, A):
        if not A:
            return [-1, -1]
        
        # binary search in the direction of column and row    
        left, up, right, down = 0, 0, len(A[0]) - 1, len(A) - 1
        while left + 1  < right or up + 1 < down:
            # determine binary search direction
            # in the column direction
            if right - left > down - up:
                # calculate center
                columnCenter = left + (right - left) / 2
                rowMaxIndex = self.findPeakByColumn(A, columnCenter, up, down)
                if self.isPeak(A, rowMaxIndex, columnCenter):
                    return [rowMaxIndex, columnCenter]
                elif A[rowMaxIndex][columnCenter] < A[rowMaxIndex][columnCenter - 1]:
                    right = columnCenter
                else:
                    left = columnCenter
            # in the row direction        
            else:
                rowCenter = up + (down - up) / 2
                columnMaxIndex = self.findPeakByRow(A, rowCenter, left, right)
                if self.isPeak(A, rowCenter, columnMaxIndex):
                    return [rowCenter, columnMaxIndex]
                elif A[rowCenter][columnMaxIndex] < A[rowCenter - 1][columnMaxIndex]:
                    down = rowCenter
                else:
                    up = rowCenter
        
        for row in [up, down]:
            for col in [left, right]:
                if self.isPeak(A, row, col):
                    return [row, col]
        return [-1, -1]
    
    # check if it is peak by definition    
    def isPeak(self, A, x, y):
        return A[x][y] > max(A[x][y - 1], A[x][y + 1], A[x - 1][y], A[x + 1][y])
    
    # find peak in the specified column
    def findPeakByColumn(self, A, column, up, down):
        maxValue = -sys.maxint
        maxIndex = -1
        for index in range(up, down + 1):
            if A[index][column] > maxValue:
                maxValue = A[index][column]
                maxIndex = index
        return maxIndex
    
    # find peak in the specified row
    def findPeakByRow(self, A, row, left, right):
        maxValue = -sys.maxint
        maxIndex = -1
        for index in range(left, right + 1):
            if A[row][index] > maxValue:
                maxValue = A[row][index]
                maxIndex = index
        return maxIndex
'''Summary
'''