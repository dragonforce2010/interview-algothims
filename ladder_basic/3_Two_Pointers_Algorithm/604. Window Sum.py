'''
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.

Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
'''
class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        n = len(nums)
        if n < k or k <= 0:
            return []
        
        sums = [0] * (n - k + 1)
        
        for i in range(k):
            sums[0] += nums[i]
        
        for i in xrange(1, n - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i + k - 1]

        return sums

'''
算法武器：窗口和（利用windowSum[i - 1] 计算 windowSum[i]）
计算公式需要熟记：

sums[i] = sums[i - 1] - nums[i] + nums[i + k - 1]
窗口和的个数计算：

	windowSumCount = n - k + 1
算法思路：

参数合法性检查
初始化窗口和数组，开辟空间，窗口和数组长度为n - k + 1
计算第一个窗口和sums[0]，因为后面的窗口和都会由前一个窗口和递推出来
for循环遍，求解所有的窗口和sums[i], 例如如下公式
sums[i] = sums[i - 1] - nums[i] + nums[i + k - 1]
'''