'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example
Given array [3,2,3,1,2], return 1.
'''
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        profit = 0
        low = prices[0]

        for price in prices:
            profit = max(profit, price - low)
            low = min(low, price)

        return profit

'''
算法武器：数组 + 一次遍历(打擂台法)

http://www.cnblogs.com/felixfang/p/3644768.html
股票问题：
想要最大化收益就是buy low sell high
扫描价格数组，不断用当前价格减去历史最低点计算收益，如果大于历史收益，则将其更新

如果发现新的股票新低就将其更新

因为题目只要求进行一次交易，所以total不是累加的，而是在不同的收益中选取某次交易最大的收益🉐
'''