'''
Given some points and a point origin in two dimensional space, find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
'''
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import heapq
class Type:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __cmp__(self, other):
        if other.dist != self.dist:
            return other.dist - self.dist
        if other.point.x != self.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y
        
class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        self.heap = []
        for point in points:
            dist = self.getDistance(point, origin)
            heapq.heappush(self.heap, Type(dist, point))
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        ret = []
        while self.heap:
            ret.append(heapq.heappop(self.heap).point)
     
        ret.reverse()
        return ret
    
    def getDistance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
'''
算法武器：heap

看到求最近的几个点、最大、最小的几个点等问题，都是使用堆来进行求解

注意：
距离不同的，则按照距离比较，并且返回
因为我们希望每次出堆的元素是距离最大的，而距离小的都保存在堆呢所以以下我们就实现一个大根堆
所以比较方法都是用other - self，按照降序排列
'''