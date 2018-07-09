'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
class Solution:
    pass


'''
算法武器： 动态规划

本题和Jump Game I的区别是
Jump Game要求求可行性，是否能够从起始点调到最后一个点
Jump Game II要求求出最短跳跃次数
这个程序大致框架相同，仅在dp[i]求解/赋值方面略有不同
'''