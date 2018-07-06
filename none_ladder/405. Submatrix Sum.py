'''
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of the left-up and right-down number.

Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]

Challenge
O(n3) time.
'''
class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    本题解法的时间复杂度为O(n^4)
    """
    def submatrixSum(self, matrix):
        # write your code here
        if not matrix:
            return []
            
        m, n = len(matrix), len(matrix[0])
        # 初始化矩阵的前缀和，同样我们总是在每个维度上多开辟一个空间，这样比较好表示前0项前缀和的概念
        presum = [ [0] * (n + 1) for _ in range(m + 1)]
        
        # 用两个for循环，从1开始滚动计算前缀和
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 根据矩阵前缀和计算公式计算从（0，0）-> (i - 1, j - 1)的前缀和
                # 注意：这里的i，j表示前i行，前j列，所以对应到下标是(i - 1, j - 1)
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] - presum[i - 1][j - 1] + matrix[i - 1][j - 1]
                # 再用一个for循环遍历子矩阵的可能的起点位置，然后计算(x,y) -> (i - 1, y - 1)的前缀和，检查其是否为0
                for x in range(i):
                    for y in range(j):
                        if presum[i][j] == presum[i][y] + presum[x][j] - presum[x][y]:
                            return [[x, y], [i - 1, j - 1]]
                            
        return []

'''
算法武器：二维矩阵前缀和 + 二维矩阵区间和

注意：

我们不仅知道对于一维数组有一个前缀和的概念，我们也知道对于矩阵也有前缀和的概念
数组前缀和： sum[i] = sum[i - 1] + num[i]
数组区间和：sum[i, j] = sum[j] - sum[i - 1]
矩阵前缀和：sum[i, j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + matrix[i][j]
矩阵区间和：sum[(m, n), (i, j)] = f[i][j] - sum[i][n] - sum[m][j] + sum[i][j]
算法思路：

首先使用两层for循环遍历求解矩阵的sum[i][j], 即从(0, 0) 到 (i, j)的前缀和
然后在第二层for循环内部进行两层嵌套for循环，这个for循环用于遍历子矩阵的起点(m, n), 查看子矩阵(m, n) -> (i, j)是否和为0，使用上面的矩阵区间和公式即可
本题目将前缀和的概念和应用扩大到了矩阵。
F[i][j]代表子矩阵【（0, 0）， （i - 1, j - 1）】的前缀和
i,j 是位置不是下标，所以f在定义时在行列方向都多开了一个空间

矩阵的前缀和计算公式：
f[i][j] = f[i-1][j] + f[i][j-1] - f[i-1][j-1] + matrix[i-1][j-1]

矩阵的子区间/子矩阵的和的计算公式：
f[i][j] - ( f[i][n] + f[m][j] - f[m][n] )
'''