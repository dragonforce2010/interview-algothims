'''Description
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number
Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]
'''
class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    # solution1: O(n^4)
    def submatrixSum(self, matrix):
        # Write your code here
        lenM = len(matrix)
        lenN = len(matrix[0])

        # for i in xrange()

        if lenM == lenN == 1 and matrix[0][0] == 0: 
            return [[0, 0], [0, 0]]
        
        # f[i][j]: sum of submatrix [(0, 0), (i - 1, j - 1)]
        f = [[0] * (lenN + 1) for y in xrange(lenM+1)]

        for i in xrange(1, lenM+1):
            for j in xrange(1, lenN+1):
                # calculate matrix [(0, 0), (i, j)]
                f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1][j-1] + matrix[i-1][j-1]
                # loop through all the starting pos of matrix
                for m in xrange(i):
                    for n in xrange(j):
                        # calculate submatrix [(m,n), (i, j)]
                        if f[i][j] == f[i][n] + f[m][j] - f[m][n]:
                            return [[m, n], [i-1, j-1]]
        
        return []                    
                            
    # # solution2: O(n^3)
    # def submatrixSum(self, matrix):
    #     if not matrix:
    #         return []
            
    #     m, n = len(matrix), len(matrix[0])
    #     presum = [[0] * (n + 1) for _ in range(m + 1)]
        
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + matrix[i - 1][j - 1]
        
    #     dict = {0: 1}   
    #     for x1 in range(0, m + 1):
    #         for x2 in range(x1 + 1, m + 1):
    #             for y in range(0, n + 1):
    #                 localsum = presum[x2][y] - presum[x1][y]
    #                 if localsum == 0:
    #                     print("hahahah:", x1, x2, y)
    #                     return [[x1, 0], [x2 - 1, dict[localsum] - 1]]
                        
    #                 if localsum in dict:
    #                     y1 = dict[localsum]
    #                     return [[x1, y1], [x2 - 1, y - 1]]    
    #                 else:
    #                     dict[localsum] = y
                        
    #     return []                
    
    '''Summary
    算法武器：二维矩阵前缀和 + 二维矩阵区间和
注意：
- 我们不仅知道对于一维数组有一个前缀和的概念，我们也知道对于矩阵也有前缀和的概念
- 数组前缀和： sum[i] = sum[i - 1] + num[i]
- 数组区间和：sum[i, j] = sum[j] - sum[i - 1]
- 矩阵前缀和：sum[i, j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + matrix[i][j]
- 矩阵区间和：sum[(m, n), (i, j)] = f[i][j] - sum[i][n] - sum[m][j] + sum[i][j]

算法思路：
- 首先使用两层for循环遍历求解矩阵的sum[i][j], 即从(0, 0) 到 (i, j)的前缀和
- 然后在第二层for循环内部进行两层嵌套for循环，这个for循环用于遍历子矩阵的起点(m, n), 查看子矩阵(m, n) -> (i, j)是否和为0，使用上面的矩阵区间和公式即可

本题目将前缀和的概念和应用扩大到了矩阵。
F[i][j]代表子矩阵【（0, 0）， （i - 1, j - 1）】的前缀和
i,j 是位置不是下标，所以f在定义时在行列方向都多开了一个空间

矩阵的前缀和计算公式：
f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1][j-1] + matrix[i-1][j-1]

矩阵的子区间/子矩阵的和的计算公式：
f[i][j] - ( f[i][n] + f[m][j] - f[m][n] )
'''