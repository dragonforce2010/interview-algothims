'''
Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.

Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
'''
class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        l, r = min(nums), max(nums)
        n = len(nums)
        preSum = [0] * (n + 1)
        
        while r - l >= 1e-6:
            mid, find = (l + r) / 2.0, False
            minPre = 0
            for i in range(1, n + 1):
                preSum[i] = preSum[i - 1] + nums[i - 1] - mid
                # only when i >= k, then we can start checking, because we eed make sure our subarray is at least k elements
                if i >= k and preSum[i] - minPre >= 0:
                    find = True
                    break
                
                # only when i >= k, we can start updating minPre, because we need to makes sure that the subarray formed by minPre and preSum[i] contains at least k elements 
                if i >= k:
                    minPre = min(minPre, preSum[i - k + 1])

            if find:
                l = mid
            else:
                r = mid
                
        return l
'''
算法武器：二分法 + 前缀和数组 + 求average转求sum技巧 + 求基于前缀和的求最大子区间技巧

思想：transformation思想，即当一个问题已形式A出现不好求解时，我们把它转换成另一种形式，对原问题进行等价变形。本题中对average的求解转换为么个元素减去区间中值后的求和问题，这就是一个等价变化。

本题求的移动平均确实很有难度，我们使用了将求average转为求sum的技巧，即将前缀和数组中的每一位都减去mid，或者就是对数组中的每一位都减去mid，这样对减后的数组求和，如果大于零就知道存在子区间，使得其均值average大于mid
在求解区间和时，我们需要求最大子区间和，我们通过使用一遍扫描计算前缀和的同时记录最下前缀和，这样两者相减就是最大子区间和，这个技巧非常实用。
九章分析：

题意
先解读一下题意，题意是让我们求出给出的序列中所有长度大于k的子序列中平均值最大的。

解决思路
这个问题我们可以用二分查找来解决。首先先解释一下为什么我们用二分去解决，因为这个问题显然我们是不能通过暴力查找每一个序列得到最大值的，复杂度肯 定过高。所以这里我们采取的方法是反过来二分答案，再判断是否达到要求。那么问题就变成了如何去二分这个答案，怎么去一步一步缩小这个范围。

具体的解决方法
二分查找的话肯定是在一个范围内不断的二分再判断去查找，那这里的判断我们要怎么去处理呢。这里我们可以用一个数组 记录每一位减去我们当前这个区间的中值的前缀和(也就是从0到这个位置的所有数的和)。然后对这个前缀和进行判断，一边 记录，一边存储一下当前的最小值，如果遇到某一个区间的和比我们记录的最小值大，那么说明答案应该比中值大，往右边扩展，反之往左边扩展。这样反复的缩小区间，最后就能够得到最后的答案。

解法是二分答案，先确定一个答案mid，再判断是否存在连续大于等于k个数的和 大于mid
这里有一个技巧是，把每个数字减去mid，这样就把average问题变成了sum问题，只需要记录前缀中最小的那个（min_pre），要注意只求k个位置之前的前缀，保证sum[i] - min_pre至少有k个数字
'''