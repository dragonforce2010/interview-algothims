'''Description
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.
'''
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        if reader.get(0) == target:
            return 0
            
        index = 1
        while reader.get(index) < target:
            index *= 2
            
        start, end = index // 2, index
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            # 注意我们在>=的条件是更新上边界end，因为我们想找到第一个符合条件的解，这个数组中可能有重复元素存在    
            elif reader.get(mid) >= target:
                end = mid
                
        if reader.get(start) == target:
            return start
            
        if reader.get(end) == target:
            return end
            
        return -1
'''Summary
算法武器：二分法 + 降级思想 + 倍增思想

降级思想：

简化问题，去除约束，求解最简单情形，然后再逐步添加约束，求解- 复杂情形。
本题的数组是无限的，所以我们先把这个条件去掉，将问题简化为有限排序数组的搜索问题，这样就好解了，我们使用二分法就好
然后我们把无限这个条件加回去，我们发现对于二分法的end指针的初始化没法做了，因为我们不知道end在哪，所以问题转化为先找到这个end指针，这个边界，再使用二分法
寻找end边界的方法是倍增思想
倍增思想：

当我们扩容时，我们每次扩容当前尺寸的整数倍，使尺寸变为之前的两倍
当我们搜索时，我们每次搜索的步长不是常数，而是一个倍增的变数，每次跳跃的步长是上一次的2倍
以上就是倍增思想
对于本题而言，倍增思想能够让我们在logn的时间内找到end的边界

'''