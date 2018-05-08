'''Description
Given n items with size nums[i] which an integer array and all positive numbers, no duplicates. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may be chosen unlimited number of times

Have you met this question in a real interview? 
Example
Given candidate items [2,3,6,7] and target 7,

A solution set is: 
[7]
[2, 2, 3]
return 2
'''
class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackIV(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for a in nums:
            for j in xrange(a, target+1):
                dp[j] += dp[j - a]

        return dp[target]
'''Summary
注意：元素可以重复

思路：遍历item数组中的每一个元素，针对每一个元素，给其机会去更新每一个可能的体积。

对于体积j而言，item a能够贡献给总方案数的个数为dp[j - a], 因为我们选择a的方案数dp[j - a + a]相对于没选a之前的方案数dp[j -a]是相同的，如果dp[j - a]的方案数为0，那么dp[j]就也为0

再简单解释一下：
比如就j = 8, a = 5, 我们看看元素5能够对最终方案数dp[8]的影响。
我们先求出dp[8 - 5] = dp[3]的方案数，我们假设dp[3] = 20, 那么对于每一个dp[3]的方案中我们都加入元素5，这样就获得了加入5之后对dp[8]的方案的贡献，记为dp[8]'，加入元素5之后，这个dp[8]的方案数就可以更新为dp[8] += dp[8]'

因为本题不是坐标型动态规划，所以我们为dp数组开target + 1个空间， 这样dp[target]就是我们要求得解
'''