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
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
            
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid / n][mid % n] == target:
                return True
            if matrix[mid / n][mid % n] > target:
                end = mid
            else:
                start = mid
        
        if matrix[start / n][start % n] == target:
            return True
        if matrix[end / n][end % n] == target:
            return True
            
        return False
'''
算法武器：二分法 + 降维

算法要点：

因为整个矩阵是满足严格单调的，所以我们可以把二维转化为1维以简化问题
掌握二维和一维坐标的转化方式
核心精华代码：

		start, end = 0, m * n - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid / n][mid % n] == target:
                return True
            if matrix[mid / n][mid % n] > target:
                end = mid
            else:
                start = mid
'''