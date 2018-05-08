'''Description
Given n items with size nums[i] which an integer array and all positive numbers. An integer target denotes the size of a backpack. Find the number of possible fill the backpack.

Each item may only be used once

Have you met this question in a real interview? 
Example
Given candidate items [1,2,3,3,7] and target 7,

A solution set is: 
[7]
[1, 3, 3]
return 2
'''
class Solution:
    # @param {int[]} nums an integer array and all positive numbers
    # @param {int} target an integer
    # @return {int} an integer
    def backPackV(self, nums, target):
        # Write your code here
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for a in nums:
            for j in xrange(target, a - 1, -1):
                dp[j] += dp[j - a]

        return dp[target]
'''Summary
'''