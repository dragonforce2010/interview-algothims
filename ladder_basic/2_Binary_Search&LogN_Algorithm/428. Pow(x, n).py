'''Descriptiion
Implement pow(x, n).

Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1
Challenge
O(logn) time
'''
class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        # 这块使用了数学公式处理n为负数的情形
        if n < 0:
            x = 1 / x
            n = -n
            
        ans = 1
        tmp = x
        
        
        # 使用2分的方式将O(n)复杂度降低为O（logn）级别
        # 本题是2分相除的类型
        while n > 0:
            # 注意随着n的不断除2，最终n会变成1，算法结束的时候这个if block一定会被执行，计算出ans
            # 如果给定n是奇数，则以下if block会被执行两次，一次是最开始进入while循环时，一次是在while即将退出时
            if n % 2 == 1:
                ans = ans * tmp
            tmp *= tmp
            n //= 2
            
            
        return ans

'''Summary
算法武器：二分法FirstIndexOfTarget + 二分法LastIndexOfTarget

算法思想：

求出目标元素首次出现的位置firstIndex和最后一次出现的位置lastIndex
判断是否这两个位置的值不为-1，即目标元素是否存在于数组中，如果不存在则返回0
如果存在则答案为： lastIndex - firstIndex + 1

'''