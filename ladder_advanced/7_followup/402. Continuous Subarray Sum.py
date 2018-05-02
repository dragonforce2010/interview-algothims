'''Description
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)
Example
Give [-3, 1, 3, -3, 4], return [1,4].
'''
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        maxmumPresum, presum = -sys.maxint, 0
        start, end = 0, 0
        section = [0, 0]
        for i in range(len(A)):
            if presum < 0:
                presum = A[i]
                start = end = i
            else:
                presum += A[i]
                end = i
            if maxmumPresum < presum:
                maxmumPresum = presum
                section = [start, end]
        return section
'''Summary
算法武器：同方向双指针 + 一次数组扫描
利用双指针技法，都是前向型的，在从左往右扫描数组的过程中寻找最优的区间的起止点。
总结：向向型双指针一次扫描确定具有最大和的最优子区间
Awesome！

算法思路：
- start, end初始化为0， 双指针同方向一遍扫描数组
- 维护一个section变量，作为结果返回
- 维护一个全局最大子区间和maxmumSum
- 维护当前累加和sum，注意这个sum不是前缀和，而是代表区间的累加和
- 当sum累加编程负数的时候，我们对其进行丢弃，重新当当前游标i作为start和end的初值
- 否则将继续自动累加A[i], 并且更新end
- 将当前sum和全局sum比较，如果比全局大，则对全局进行更新，同时更新全局答案
'''