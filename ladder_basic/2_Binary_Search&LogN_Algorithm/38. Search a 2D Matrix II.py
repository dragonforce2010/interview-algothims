'''
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

Challenge
O(m+n) time and O(1) extra space
'''
class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix[0] == []:
            return 0
         
        count = 0
        row, column = len(matrix), len(matrix[0])
        x, y = row - 1, 0
        while x >= 0 and y < column:
            if matrix[x][y] < target:
                y += 1
            elif matrix[x][y] > target:
                x -= 1
            else:
                count += 1
                x -= 1
                y += 1
        return count
'''
算法武器：基于有序矩阵的搜索（自底向上，从左到右）

题型：二维矩阵的搜索策略
本题给定的条件是矩阵在row方向和col方向都是升序的，所以我们搜索时可以充分利用这个条件。
搜索策略

从最后一行的行首进行，使用while循环持续进行直到x或者y走出边界
如果矩阵元素小于target，那么就向右走，不可能向下走，因为我们是从最下层走起的
如果矩阵元素大于target，那么就向上移动一行，列坐标还是不变的
如果遇到矩阵元素等于target，那么就向上走一行，同时列坐标向右走一行，并且进行计数
最后返回计数
'''