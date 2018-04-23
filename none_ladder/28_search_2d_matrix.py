'''Description
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
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return False
            
        # 将二维数组拉成一维数组
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] < target:
                start = mid
            elif matrix[x][y] == target:
                return True
            else:
                end = mid
                
        x, y = start // n, start % n
        if matrix[x][y] == target:
            return True
            
        x, y = end // n, end % n
        if matrix[x][y] == target:
            return True
            
        return False

'''Summary
算法武器：二分法 + 降维
算法要点：
- 因为整个矩阵是满足严格单调的，所以我们可以把二维转化为1维以简化问题
- 掌握二维和一维坐标的转化方式
'''