'''Description
There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.
Example
For [4, 1, 1, 4], in the best solution, the total score is 18:

1. Merge second and third piles => [4, 2, 4], score +2
2. Merge the first two piles => [6, 4]，score +6
3. Merge the last two piles => [10], score +10
Other two examples:
[1, 1, 1, 1] return 8
[4, 4, 5, 9] return 43
'''
class Solution:
    # @param {int[]} A an integer array
    # @return {int} an integer
    def stoneGame(self, A):
        n = len(A)
        if n < 2:
            return 0
            
        # dp[i][j]: from pos x to j, the minimum total score of stone game    
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        sum = [[0 for _ in xrange(n)] for _ in xrange(n)]
        
        # 0, 1, 2, ... n-2, n-1
        # calculate basic dp values
        # Initialize dp[i][i] = 0
        for i in xrange(n):
            dp[i][i] = 0
        for i in xrange(0, n-1):
            dp[i][i+1] = A[i]+A[i+1]

        # initailize 2d prefixSum
        for i in xrange(n):
            sum[i][i] = A[i]
            for j in xrange(i+1, n):
                sum[i][j] = sum[i][j-1] + A[j]
        
        # calculate dp[i][j] based on state transfer equation    
        # dx: the difference between i and j, [2, n - 1]
        for dx in xrange(2, n):
            i = 0
            # j = i + x, j has to be less than n
            while i + dx < n: 
                j = i + dx
                # k: [i, j - 1]
                k = i 
                dp[i][j] = sys.maxint
                # try all the possible pos k to split section [i, j] into two sections [i, k] and [k + 1, j]
                # sum[i][k], sum[k+1][j] is the score of mergering two sections
                # note: k == j is the same as k == i, so here k can't be equal to j
                # search best ans in section [i, j]
                while k < j:
                    # t = dp[i][k] + dp[k+1][j] + sum[i][k] + sum[k+1][j]
                    t = dp[i][k] + dp[k+1][j] + sum[i][j]
                    # minimize the score of section [i, j]
                    dp[i][j] = min(dp[i][j], t)
                    k += 1
                i += 1
        return dp[0][n-1]   

'''Summary
心得总结：
看到数组，看到求最值，就得想到区间，想到起始坐标，想到二维动归。本题的动归是二维，表示在区间内的答案/状态。题目的解为整个区间内的答案。
本题动归的初始化和平常有些不同，普通动归一般初始化第一行，第一列，本题初始化的是对角线和相邻元素
本题状态方程的求解使用了将大区间划分成小区间的方式，使用k位置将区间一分为二，化繁为简，建立动归之间的递归关系
本题的思想中还有分治，是分治法和动归的结合

题目分析：f[l][r]表示把l~r这些石子堆合并成一堆的最小花费
枚举k，f[l][k] + f[k+1][r] + sum[l][r] 表示我们先把l~k合并成一堆A，再把k+1~r合并成一堆B，接下来我们把A和B合并，就成功的把l~r合并成了一堆。A和B合并的代价就是l~k的石子的个数和k+1~r的石子的个数总和，就是l~r的石子个数总和，即sum[l][r]
'''