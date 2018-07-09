'''
Implement int sqrt(int x).

Compute and return the square root of x.

Example
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

Challenge
O(log(x))
'''
class Solution:
    def sqrt(self, x):
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                start = id
            else:
                end = mid

        if end ** 2 <= x:
            return end

        return start
