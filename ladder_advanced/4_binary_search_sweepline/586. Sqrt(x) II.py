'''Description
Implement double sqrt(double x) and x >= 0.

Compute and return the square root of x.

 Notice
You do not care about the accuracy of the result, we will help you to output results.
Example
Given n = 2 return 1.41421356
'''
class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # Write your code here

        left, right = 0.0, x
        eps = 1e-12
        
        if x < 1.0:
            right = 1.0
        
        while right - left > eps:
            mid = left + (right - left) / 2
            if mid * mid < x:
                left = mid
            else: 
                right = mid

        return left
'''Summary
算法武器：二分法
注意：
设计到浮点数的比较大小，需要用一个精度来控制，比如eps = le-12.
solution中while的循环条件是：

    right - left > eps
'''