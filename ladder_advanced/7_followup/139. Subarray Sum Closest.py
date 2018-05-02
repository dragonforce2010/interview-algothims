'''Description
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.
Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

Challenge 
O(nlogn) time
'''
class Node:
    def __init__(self, _value, _pos):
        self.value = _value
        self.pos = _pos
    
    
    def __cmp__(self, other):
        if self.value == other.value:
            return self.pos - other.pos
        return self.value - other.value 
    
        
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

        
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []
            
        presumList, presum = [], 0
        
        for x in xrange(len(nums)):
            presum += nums[x]
            presumList.append(Node(presum, x))

        presumList.sort()
        results, minSubArrSum = [0, 0], sys.maxint
        
        for i in xrange(len(presumList) - 1):
            if presumList[i + 1].value - presumList[i].value < minSubArrSum:
                minSubArrSum = presumList[i + 1].value - presumList[i].value
                results[0] = min(presumList[i + 1].pos, presumList[i].pos) + 1          
                results[1] = max(presumList[i + 1].pos, presumList[i].pos)

        return results
'''
算法武器：前缀和 + 排序 + 自定义对象
排序的前缀和有助于帮助我们解决最近子区间和的问题

算法思路：
- 本题要求解子区间和最接近0的，那么我首先要想到如何利用前缀和求子区间的和
- 子区间和要接近0，那么前缀和就要足够接近，所以这要求我们队前缀和进行排序
- 由于排序后，我们需要知道前缀和的小标，那么我们需要自定义一个复杂的对象来封装前缀和及其下标
- 在排过序的前缀和数组上我们让后一项减去前一项，逐一比较，选择全局最小的两个前缀和的差，这两个前缀和的小标就是答案
- 由于我们不知道小标哪个先与哪个后，所以我们需要对输出的坐标通过min，max运算获得下届和上届

    results[0] = min(s[i+1].pos, s[i].pos) + 1          
    results[1] = max(s[i+1].pos, s[i].pos)
'''