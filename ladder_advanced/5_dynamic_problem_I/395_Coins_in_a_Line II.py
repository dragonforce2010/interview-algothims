'''Descrition
There are n coins with different value in a line. Two players take turns to take one or two coins from left side until there are no more coins left. The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?
Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.

'''
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        if not values or len(values) <= 2:
            return True
            
        if len(values) == 3 and values[0] + values[1] > sum(values) / 2:
            return True
        else:
            return False
        
        n = len(values)    
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = values[0]
        dp[2] = values[0] + values[1]
        dp[3] = values[0] + values[1]
        
        for i in range(4, n + 1):
            dp[i] = max(values[i] + min(dp[i - 2], dp[i - 3]), \
                        values[i] + [values[i + 1]] + min(dp[i - 3], dp[i - 4]))
                        
        return dp[n]
     
    
    
    # def firstWillWin(self, values):
    #     n = len(values)
    #     if n <=2:
    #         return True
        
    #     # dp[i]: from pos i to end(n - 1), the max value the first player can get
    #     # dp = [0] * (n + 1)
    #     # dp[n] = 0
    #     dp = [0] * n
    #     dp[n - 1] = values[n - 1]
    #     dp[n - 2] = values[n - 2] + values[n - 1]
    #     dp[n - 3] = values[n - 3] + values[n - 2]
        
    #     for i in xrange(n - 5, -1, -1):
    #         dp[i] = max(\
    #                     # If the first player choose one, the second player may choose one or two situation
    #                     values[i] + min(dp[i + 2], dp[i + 3]), \
    #                     # If the first player choose two, the second player may choose one or two situation
    #                     values[i] + values[i + 1] + min(dp[i + 3], dp[i + 4]))
        
    #     # dp[0]: from pos 0 to end(n - 1), the max value the first player can get
    #     # if dp[0] is more than half of the sum, the first player will win
    #     return dp[0] > sum(values) / 2
'''Summary
http://www.cnblogs.com/grandyang/p/5864323.html
这道题是之前那道Coins in a Line的延伸，由于每个硬币的面值不同，所以那道题的数学解法就不行了，这里我们需要使用一种方法叫做极小化极大算法Minimax，这是博弈论中比较经典的一种思想，LeetCode上有一道需要用这种思路解的题Guess Number Higher or Lower II。这道题如果没有接触过相类似的题，感觉还是蛮有难度的。我们需要用DP来解，我们定义一个一维数组dp，其中dp[i]表示从i到end可取的最大钱数，大小比values数组多出一位，若n为values的长度，那么dp[n]先初始化为0。我们是从后往前推，我们想如果是values数组的最后一位，及i = n-1时，此时dp[n-1]应该初始化为values[n-1]，因为拿了肯定比不拿大，钱又没有负面额；那么继续往前推，当i=n-2时，dp[n-2]应该初始化为values[n-2]+values[n-1]，应为最多可以拿两个，所以最大值肯定是两个都拿；当i=n-3时，dp[n-3]应该初始化为values[n-3]+values[n-2]，因为此时还剩三个硬币，你若只拿一个，那么就会给对手留两个，当然不行，所以自己要拿两个，只能给对手留一个，那么到目前位置初始化的步骤就完成了，下面就需要找递推式了：

当我们处在i处时，我们有两种选择，拿一个还是拿两个硬币，我们现在分情况讨论：

当我们只拿一个硬币values[i]时，那么对手有两种选择，拿一个硬币values[i+1]，或者拿两个硬币values[i+1] + values[i+2]
a) 当对手只拿一个硬币values[i+1]时，我们只能从i+2到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+2]
b) 当对手拿两个硬币values[i+1] + values[i+2]时，我们只能从i+3到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+3]
由于对手的目的是让我们拿较小的硬币，所以我们只能拿dp[i+2]和dp[i+3]中较小的一个，所以对于我们只拿一个硬币的情况，我们能拿到的最大钱数为values[i] + min(dp[i+2], dp[i+3])

当我们拿两个硬币values[i] + values[i + 1]时，那么对手有两种选择，拿一个硬币values[i+2]，或者拿两个硬币values[i+2] + values[i+3]
a) 当对手只拿一个硬币values[i+2]时，我们只能从i+3到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+3]
b) 当对手拿两个硬币values[i+2] + values[i+3]时，我们只能从i+4到end之间来取硬币，所以我们能拿到的最大硬币数为dp[i+4]
由于对手的目的是让我们拿较小的硬币，所以我们只能拿dp[i+3]和dp[i+4]中较小的一个，所以对于我们只拿一个硬币的情况，我们能拿到的最大钱数为values[i] + values[i + 1] + min(dp[i+3], dp[i+4])

综上所述，递推式就有了 dp[i] = max(values[i] + min(dp[i+2], dp[i+3]), values[i] + values[i + 1] + min(dp[i+3], dp[i+4]))
这样当我们算出了dp[0]，知道了第一个玩家能取出的最大钱数，我们只需要算出总钱数，然后就能计算出另一个玩家能取出的钱数，二者比较就知道第一个玩家能否赢了，参见代码如下：
'''