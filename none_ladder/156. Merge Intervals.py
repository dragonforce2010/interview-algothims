'''
Given a collection of intervals, merge all overlapping intervals.

Example
Given intervals => merged intervals:

[                     [
  (1, 3),               (1, 6),
  (2, 6),      =>       (8, 10),
  (8, 10),              (15, 18)
  (15, 18)            ]
]
Challenge
O(n log n) time and O(1) extra space.
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return []
            
        # 对区间进行排序
        sortedIntervals = sorted(intervals, key = lambda interval: interval.start)
        result = []
        
        for interval in sortedIntervals:
            # 对于没有区间冲突的情形，只需单纯加入新区间
            if not result or result[-1].end < interval.start:
                result.append(interval)
            # 如果有区间冲突，该冲突会影响到上一个区间的end，需要对其更新
            # 不需要担心更新start，因为我们的区间是按start进行排序的
            else:
                result[-1].end = max(result[-1].end, interval.end)
                
        return result
