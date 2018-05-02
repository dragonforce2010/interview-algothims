'''Description
There is a stone game.At the beginning of the game the player picks n piles of stones in a circle.

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
    def stoneGame2(self, A):
        # Write your code here
        n = len(A)
        if n <= 1:
            return 0

        s = [0]
        dp = [[sys.maxint] * (2 * n) for j in xrange(2 * n)]
        for i in xrange(2 * n):
            s.append(s[-1] + A[i % n])
            dp[i][i] = 0

        for l in xrange(2, 2 * n + 1):
            for i in xrange(2 * n):
                j = i + l - 1
                if j >= 2 * n:
                    continue
                for k in xrange(i, j):
                    dp[i][j] = min(dp[i][k] + dp[k+1][j] + s[j + 1] - s[i], dp[i][j])

        ans = sys.maxint
        for i in xrange(n):
            ans = min(ans, dp[i][i + n - 1])
        return ans

'''Summary
这个题目里面说明了，所有的石子围成一个圆
也就是说，第一个和最后一个是连在一起的
也就是说，第一个和最后一个是可能合并的
答案给的处理方式是，把所有的再复制一份，放在最后一个石子的后面，这样就可以“连”着了
len <= n是可以的
i + len - 1 < 2 * n是必须的，因为要考虑首尾相连的部分

因为这是一个环，答案一定是环上某处断开后长度为n的一个答案，所以们把n扩展成2n（复制一倍）。
那么任意长度为n的[i, i + n - 1] 都是环断开的一种方式，从所有方式中选取最大值即可。
'''
