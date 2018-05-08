'''Description
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? 
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge 
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?
'''
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        n = len(values)
        if n == 0:
            return False
            
        dp = [[0] * n for _ in xrange(n)]
        prefixSum = [0] * (n + 1) 
        prefixSum[0] = 0
        for i in xrange(1, n + 1):
            prefixSum[i] = prefixSum[i - 1]  + values[i - 1]
            if i < n:
                dp[i][i] = values[i]
            
        for start in xrange(n - 1):
            for end in xrange(i + 1, n):
                if start + 1 == end:
                    dp[start][end] = max(values[start], values[end])
                    continue
                s = prefixSum[end + 1] - prefixSum[start]
                # dp[start][end] = max(values[start] + s - values[start] - dp[start + 1][end], values[end] + s - values[end] - dp[start][end - 1])
                dp[start][end] = max(s - dp[start + 1][end], s - dp[start][end - 1])
                    
        return dp[0][n - 1] > sum(values) / 2
'''Summary
http://posts.careerengine.us/p/581ada5c1b4ada575f006fb2
定义dp(i,j)为区间(i,j)先手玩家可以取到的最大硬币总价值。

定义sum(i,j)是从i到j的区间和
首先考虑dp(i,j),可以拿第i个硬币，从dp(i+1,j)转移过来。也可以拿第j个硬币，从第dp(i,j-1)转移过来。

dp方程为dp(i,j) = max(values[i] + sum(i+1,j) - dp(i+1,j) , values[j] + sum(i,j-1) - dp(i,j-1));

其中的values[i] + sum(i+1,j) - dp(i+1,j) 可以这样理解：我拿第i个数值，values[i]是我拿到的数值，肯定要加上，再想区间(i+1,j)我能拿到的最大值是多少，由于我拿了第i个，所以区间(i+1,j)变成了对面先手，对面能够拿到最大值dp(i+1,j)，而我只能拿到sum(i+1,j)-dp(i+1,j)

由上述公式就可以写出代码了，时间复杂度O(N^2)，空间复杂度O(N^2)

可以使用滚动数组的方法对空间进行优化，达到O(N)的空间复杂度。

之前的那个公式对于写代码来说并不是很直观，注意到，上述公式dp(i,j)区间长度为j-i+1，dp(i,j-1) 和dp(i+1,j)的区间长度都是j-i，考虑到区间长度为j-i+1的区间是由区间长度为j-i的区间转化而来的。所以可以转化上述公式。

定义k为一个区间的长度。

则上述公式可以写作dp(i,i+k) = max(values[i] + sum(i+1,i+k) - dp(i+1,i+k) , values[i+k] + sum(i,i+k-1) - dp(i,i+k-1))

现在将dp的第二维定义为这个区间的长度，所以dp(i,k)的含义变成了区间(i,i+k)先手玩家可以取到的最大硬币总价值。

上述公式变为dp(i,k) = max(values[i] + sum(i+1,i+k) - dp(i+1,k-1) , values[i+k] + sum(i,i+k-1) - dp(i,k-1))

由上述的公式可以很容易的写出代码了，时间复杂度O（N^2），空间复杂度O(N^2)

其实空间复杂度还是可以优化的，第一种方法：可以滚动数组，可以把空间复杂度变为O(N)。第二种方法：与背包算法的空间优化类似，将i变成从后向前找，空间复杂度为O(N)，这个比前面一种优化方法，常数小一些。

公式变为 dp1(i) = max(values[i] + sum(i+1,i+k) - dp1(i+1) , values[i+k] + sum(i,i+k-1) - dp1(i)) i 从后向前遍历

这里有一个问题，dp1(i+1)这个值在计算dp1(i+1)的时候被改变了，但是在计算dp1(i)之中又用到了，所以在改变之前需要存储这个值。

时间复杂度O(N^2),空间复杂度O(N)

面试官角度分析：这道题是一个动态规划的问题，给出动态规划算法可以hire,如果想到
优化空间到O(N)可以达到strong hire。
'''