'''Description
Given an array of integers, find a contiguous subarray which has the largest sum.
Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge 
Can you do it in time complexity O(n)?
'''
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    
    def maxSubArray(self, nums):
        if not nums:
            return -sys.maxint
        
        maxSum, minPresum, presum = nums[0], 0, 0
        
        for num in nums:
            presum += num
            maxSum = max(maxSum, presum - minPresum)
            minPresum = min(minPresum, presum)
        return maxSum
'''Summary
算法武器：前缀和 + 区间和公式
区间和公式：

sum[i, j] = sum[j] - sum[i - 1]
本题要求最大的子数组和，这个子数组是整个数组中的一段，要求这段和，我们首先就要想到区间和计算公司，该公式由两个前缀和相减得到。

如果要保证区间和最大，我们就需要做被减数的前缀和最大，做减数的前缀和最小，这样相减后的差最大。

解法：
遍历一遍数组，记录每个前缀和，同时记录下当前前缀和、最小前缀和，最后我们
本题初始化是要注意，ans, minSum = nums[0], 0
- 因为一开始时，minSum可以什么元素都不选，所以初始化为0
- ans作为结果，至少有一个元素，所以我们使用nums[i]做初始化

注意：
- 本题的解法是一个动态过程
- 随着数组每个元素的遍历，我们动态计算当前sum，计算minSum，以及计算答案
- 整个过程是动态的
- 错误思维：我们试图用一遍扫描计算出maxSum和minSum，然后将两个相减，这样是不可以的，因为maxSum和minSum在下标上是有要求的，maxSum的终止下标必须必minSum的下标大才可以。这种错误的思维属于静态思考，没有考虑到maxSum和minSum的下标的关系。如果按照本题的解法，动态求解，那么我们可以保证我们的解释最优的。

http://www.cnblogs.com/xiehongfeng100/p/4570082.html　
基本思路是这样的，在每一步，我们维护两个变量，一个是全局最优，就是到当前元素为止最优的解是，一个是局部最优，就是必须包含当前元素的最优的解。接下来说说动态规划的递推式（这是动态规划最重要的步骤，递归式出来了，基本上代码框架也就出来了）。假设我们已知第i步的global[i]（全局最优）和local[i]（局部最优），那么第i+1步的表达式是：local[i+1]=max(A[i], local[i]+A[i])，就是局部最优是一定要包含当前元素，所以不然就是上一步的局部最优local[i]+当前元素A[i]（因为local[i]一定包含第i个元素，所以不违反条件），但是如果local[i]是负的，那么加上他就不如不需要的，所以不然就是直接用A[i]；global[i+1]=max(local[i+1],global[i])，有了当前一步的局部最优，那么全局最优就是当前的局部最优或者还是原来的全局最优（所有情况都会被涵盖进来，因为最优的解如果不包含当前元素，那么前面会被维护在全局最优里面，如果包含当前元素，那么就是这个局部最优）。
https://segmentfault.com/a/1190000003481202
思路
这是一道非常典型的动态规划题，为了求整个字符串最大的子序列和，我们将先求较小的字符串的最大子序列和。这里我们从后向前、从前向后计算都是可以的。在从前向后计算的方法中，我们将第i个元素之前最大的子序列和存入一个一维数组dp中，对第i+1个元素来说，它的值取决于dp[i]，如果dp[i]是负数，那就没有必要加上它，因为这只会拖累子序列的最大和。如果是正数就加上它。最后我们再讲第i+1个元素自身加进去，就得到了第i+1个元素之前最大的子序列和。
'''