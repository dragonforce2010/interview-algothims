'''Description
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?
Example
n = 1, return true.

n = 2, return true.

n = 3, return false.

n = 4, return true.

n = 5, return true.

Challenge 
O(n) time and O(1) memory
'''
class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # solution1: observe the number and find the secretes
        '''
        return n % 3 != 0 
        '''
        
        # solution2: dp
        # state definition: f[i] = true means the first player can win if there are i conins left, vice versa
        if n == 0:
            return False
            
        if n <= 2:
            return True
        
        f = [False] * (n + 1)
        f[0], f[1], f[2] = False, True, True
        for i in xrange(3, n + 1):
            if f[i - 1] == False or f[i - 2] == False:
                f[i] = True
        
        return f[n]
        
'''Summary
算法武器1：动态规划
算法武器2：记忆化搜索 + 递归 + 画搜索树 + 手动做实验
算法武器3：手动做实验 + 找规律 （n % 3的解法）

http://www.cnblogs.com/grandyang/p/5861500.html
http://www.cnblogs.com/grandyang/p/4873248.html
有史以来最少代码量的解法，虽然解法很简单，但是题目还是蛮有意思的，题目说给我们一堆石子，每次可以拿一个两个或三个，两个人轮流拿，拿到最后一个石子的人获胜，现在给我们一堆石子的个数，问我们能不能赢。那么我们就从最开始分析，由于是我们先拿，那么3个以内(包括3个)的石子，我们直接赢，如果共4个，那么我们一定输，因为不管我们取几个，下一个人一次都能取完。如果共5个，我们赢，因为我们可以取一个，然后变成4个让别人取，根据上面的分析我们赢，所以我们列出1到10个的情况如下：
1 Win
2 Win
3 Win
4 Lost
5 Win
6 Win
7 Win
8 Lost
9 Win
10 Win
由此我们可以发现规律，只要是4的倍数个，我们一定会输，所以对4取余即可

动态规划解法：
https://yisuang1186.gitbooks.io/-shuatibiji/coins_in_a_line.html
分析：
state: 还剩i个硬币，先取硬币的人的输赢情况（就是题目中说的first player的输赢情况）。
这个题目的条件大概就是，如果取走一个，还剩k - 1个，k - 1个是false，或者如果取走两个，还剩k - 2个，k - 2个是false，那么first player就能保证另一个人走到false的位置上，之后合理出牌就一定会赢。
'''