'''Description
Find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
'''
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        f, g = [], []
        f.append(nums[0])
        g.append(nums[0])
        for i in xrange(1, len(nums)):
            f.append(max(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
            g.append(min(f[i-1]*nums[i], g[i-1]*nums[i], nums[i]))
        m = f[0]
        for i in xrange(1, len(f)): m = max(m, f[i])
        return m
'''Summary
http://blog.csdn.net/whuwangyi/article/details/39577455
'''