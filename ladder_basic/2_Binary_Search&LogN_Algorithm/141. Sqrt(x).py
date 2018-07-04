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
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start, end = 0, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 <= x:
                start = mid
            else:
                end = mid
                
        if end ** 2 <= x:
            return end
        else:
            return start