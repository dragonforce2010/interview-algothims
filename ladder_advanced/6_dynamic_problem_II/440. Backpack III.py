'''Description
Given n kind of items with size Ai and value Vi( each item has an infinite number available) and a backpack with size m. What's the maximum value can you put into the backpack?

 Notice
You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? 
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 15.
'''
class Solution:
    # @param {int[]} A an integer array
    # @param {int[]} V an integer array
    # @param {int} m an integer
    # @return {int} an array
    def backPackIII(self, A, V, m):
        f = [0 for i in xrange(m+1)]
        for (a, v) in zip(A, V):
            for j in xrange(a, m+1):
                if f[j - a] + v > f[j]:
                    f[j] = f[j - a] + v
        return f[m]
'''Summary
这道背包问题的特点是物品可以重复放入，限定条件是体积一定，目标能够在有限体积下放入的最大价值。

for (a, v) in zip(A, V):
    for j in xrange(a, m+1):
        if f[j - a] + v > f[j]:
            f[j] = f[j - a] + v
解释一下上面这段关键的部分：
对于每个物品（a, v）, 遍历所有可能的体积a ~ m(体积得知道>= a)
对于每个可能的体积，我们尝试将a加入背包，查看是否能够增加背包的价值，如果可以，我们就更新体积为j时的背包的价值。这种加入是重复的加入的，我们不断地尝试加入a物品，知道背包满为止。

备注：

f[j - a] 代表加入a之前的背包的价值
f[j - a] + v 代表加入a之后的背包价值
'''