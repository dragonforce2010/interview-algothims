'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example
Consider the following matrix:

[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                end = mid
            else:
                start = mid

        if matrix[start // n][start % n] == target:
            return True
        if matrix[end // n][end % n] = target:
            return True

        return False