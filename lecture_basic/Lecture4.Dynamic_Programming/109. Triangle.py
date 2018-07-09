'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Example
Given the following triangle:

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
'''
class Solution:
    '''
    1. Definition
        - dp[i][j]: minmum path sum from top to (i, j)
    2. Anaswer
        - max(dp[lastRow])
    3. State transfer equation
        - dp[i][j]: min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    4. Initialization
        - dp[i][0]:dp[i - 1][0]
        - dp[i][i]:dp[i - 1][i - 1]
    '''
    def minimumTotal(self, triangle):
        if not triangle:
            return -1

        m = len(triangle)
        dp = [ [0] * (row + 1) for row in range(m)]
        dp[0][0] = triangle[0][0]

        # dp初始化
        for row in range(1, m):
            dp[row][0] = dp[row - 1][0] + triangle[row][0]
            dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]

        # 使用两层for循环求解出所有的dp状态
        for row in range(1, m):
            for col in range(1, row):
                dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col]) + triangle[row][col]

        return min(dp[m - 1])

'''
算法武器： 动态规划
求解最值问题使用dp是一种解决方案

dp[i][j]: 从三角形顶点到(i,j)位置处的path sum

对dp数组初始化的时候需要注意：我们每行元素的数量是不一样的，每行元素的数量等于当前行的行号(从1开始)，就是第i行有i个元素

dp = [[0] * (row + 1) for row in range(m)]
对三角形dp初始化时，我们只需要for一遍行就可以了，在for循环体内我们初始化dp[row][0]和dp[row][row].

for row in range(1,m):
        dp[row][0] = dp[row - 1][0] + triangle[row][0]
        dp[row][row] = dp[row - 1][row - 1] + triangle[row][row]
'''