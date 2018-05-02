'''Description
Given an array of n * m matrix, and a moving matrix window (size k * k), move the window from top left to botton right at each iteration, find the maximum sum inside the window at each moving.
Return 0 if the answer does not exist.
Example
For matrix

[
  [1, 5, 3],
  [3, 2, 1],
  [4, 1, 9],
]
The moving window size k = 2. 
return 13.

At first the window is at the start of the array like this

[
  [|1, 5|, 3],
  [|3, 2|, 1],
  [4, 1, 9],
]
,get the sum 11;
then the window move one step forward.

[
  [1, |5, 3|],
  [3, |2, 1|],
  [4, 1, 9],
]
,get the sum 11;
then the window move one step forward again.

[
  [1, 5, 3],
  [|3, 2|, 1],
  [|4, 1|, 9],
]
,get the sum 10;
then the window move one step forward again.

[
  [1, 5, 3],
  [3, |2, 1|],
  [4, |1, 9|],
]
,get the sum 13;
SO finally, get the maximum from all the sum which is 13.
'''
class Solution:
    # @param {int[][]} matrix an integer array of n * m matrix
    # @param {int} k an integer
    # @return {int} the maximum number
    def maxSlidingMatrix(self, matrix, k):
        # Write your code here
        n, m = len(matrix), len(matrix[0])
        # check if matrix size is smaller then the given window size
        if n == 0 or n < k or m == 0 or m < k:
            return 0

        # initialize prefix sum
        # sum[i][j]: sum of submatrix [(0,0), (i - 1, j - 1)]
        sum = [[0] * (m + 1) for i in xrange(n + 1)]

        # calculate sum[i][j]
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                sum[i][j] = matrix[i - 1][j - 1] + \
                            sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

        # based on prefix sum array - sum to find the target submatrix which has largest sum
        # note that: i,j in for loop represents position rather then subscript
        max_value = -sys.maxint
        for i in xrange(k, n + 1):
            for j in xrange(k, m + 1):
                # calculate submatrix of window size k
                # submatrix: [(i - k - 1, j - k - 1), (i - 1, j - 1)]
                value = sum[i][j] - sum[i - k][j] - \
                        sum[i][j - k] + sum[i - k][j - k]

                max_value = max(max_value, value)

        return max_value
'''Summary
算法武器：矩阵前缀和 + 动态规划 + 矩阵坐标定位方式（右下角的点）
此题是子矩阵前缀和类型题目，求解关键是首先使用动态规划求出这个矩阵前缀和数组sum，然后再利用sum求出子矩阵的前缀和。
由于本题限定window尺寸，所以遍历的时候注意其实节点从位置K开始

矩阵前缀和计算公式
sum[i][j] = matrix[i - 1][j - 1] + sum[i - 1][j] + sum[i][j-1] - sum[i - 1][j-1]

子矩阵前缀和计算公式
submatrixSum = sum[i][j] - sum[i - k][j] - sum[j][j-k] + sum[i-k][j-k]

注意：
- 本题在最后部分双重for循环遍历时，我们的i和j都是从k开始取值的
- 这样做的原因和我们的前缀和定义有关，sum[i][j]代表的是从（0，0）点到（i,j）点的矩阵前缀和，所以我们是使用矩阵的右下角元素来定位矩阵
- 所以这两个for循环for的就是矩阵右下角的所有可能坐标
'''