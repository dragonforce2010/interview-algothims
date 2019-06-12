'''
https://aonecode.com/amazon-online-assessment-questions

Find the k post offices located closest to you, given your location and a list of locations of all post offices available.
Locations are given in 2D coordinates in [X, Y], where X and Y are integers.
Euclidean distance is applied to find the distance between you and a post office.
Assume your location is [m, n] and the location of a post office is [p, q], the Euclidean distance between the office and you is SquareRoot((m - p) * (m - p) + (n - q) * (n - q)).
K is a positive integer much smaller than the given number of post offices. from aonecode.com

e.g.
Input
you: [0, 0]
post_offices: [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3

Output from aonecode.com
[[-1, 2], [0, 3], [4, 3]] 
'''
import heapq
class Solutoin:
    def findNearestPostOffices(self, srcx, srcy, postOffices):
        if not postOffices:
            return []

        heap = []
        for x, y in postOffices:
            dist = (srcx - x) ** 2 + (srcy - y) ** 2
            heapq.heappush(-dist, x, y)
            if len(heap) > k:
                heapq.heappop(heap)

        ans = [(heapq.heappop()[1], heapq.heappop()[2]) for i in range(k)]
        return ans
        

        
