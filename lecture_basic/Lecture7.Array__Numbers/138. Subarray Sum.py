'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''
class Solution:
    def subarraySum(self, A):
        if not A:
            return []

        cache = {0 : -1}
        sum = 0
        
        for i in range(len(A)):
            sum += A[i]
            if sum in cache:
                return [cache[sum] + 1: i]
            cache[sum] = i

        return []
'''
算法武器：一维前缀和preSum + 一维区间和 + 哈希表

sum[i,j] = sum[j] - sum[i - 1]

注意：

上面这个公式告诉我们有可能存在两个前缀和相同的情况
同时还可能存在另一种情形，即sum[j] = 0, 那么sum[i - 1] 也必须等于 0
所以我们需要给hash字典做个初始化hs = {0:-1}, 即累加和为0时，下标为-1，这样我们一旦在数组中找到sum[0 : i] = 0时，我们依然可以按照[hs[sum] + 1, i] 算出答案为[0, i]
总结：对前缀和公式的理解需要加深，不只是有两个前缀和相等这么简答，还需要考虑到某一个前缀和就是0，即数组从下标为0的地方开始到一个位置i的前缀和为零，这样我们就必须正确初始化哈希表，或者在for循环时对前缀和等于0的情形进行判断
def subarraySum(self, A):
        # 边界条件
        if not A:
            return []
        
        # 用hash字典保存区间和与下标的映射关系
        # 注意初始化：累加和为0时，下标为-1
        hs = {}
        # sum是累加和
        sum = 0
        
        # 扫描数组
        for i in range(len(A)):
            # 计算累积和
            sum += A[i]
            if sum == 0:
                return [0, i]
            # 检测累加和是否在字典中出现过
            if sum in hs:
                return [hs[sum] + 1, i]
            # 将累加和sum作为k，此时下标i存入字典
            hs[sum] = i
        
        return [] 
遍历一遍数组，同时不断求出所有位置的前缀和，并且将其放到hash中。如果当前前缀和能够在hash中找到，那么就意味着数组中存在两个一样的前缀和，那么根据数组区间求和公式：
sum[i, j] = sum[j] - sum[i - 1]
两个相等的前缀和一定导致数组中某个区间的和为0

我们遍历过程中，当找到了一样的前缀和时，那个首先放在hash表中的是下标i - 1,我们需要将其➕1才能获得正确答案，即

[hs[sum] + 1, i]
'''