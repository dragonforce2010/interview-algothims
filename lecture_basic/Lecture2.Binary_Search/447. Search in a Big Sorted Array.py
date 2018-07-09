'''
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.
'''
class Solution:
    def searchBigSortedArray(self, reader, target):
        if not reader:
            raise Exception('Invalid parameter!')

        index = 1
        while reader.get(index) < target:
            index *= 2

        start, end = index // 2, index
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1