'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return 2147483647

Example
Given dividend = 100 and divisor = 9, return 11.
'''
class Solution:
    # @param {int} dividend the dividend
    # @param {int} divisor the divisor
    # @return {int} the result
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        
        if divisor == 0:
            return INT_MAX
        
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        y, x = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        
        while shift >= 0:
            if y >= x << shift:
                y -= x << shift
                ans += 1 << shift
            shift -= 1
        
        if neg:
            ans = - ans
        
        if ans > INT_MAX:
            return INT_MAX
        
        return ans

'''
算法武器：位操作 + 除法转化为乘减法

掌握以下除法转化为乘法和减法的公式

y = ax + b => y / x = a
上式子表示：我们把两个数的除法变成了求系数a的过程

y = 2^c1 * x + 2^c2 * x + ... + b =>
y/x = c1 + c2 + ....
上面的式子表示：我们把a转换为了多个2进制幂次的表示，最终系数a的值为：c1 + c2 + ...
注：将a转成多个2进制幂次的表示使得我们能够使用位运算（用左移代表乘2）

两数相除不能用除法那就使用乘减，同时乘可以使用移位来进行
可以使用一个变量记录符号，然后将除数和被除数都取绝对值进行运算。

整数的最大位数为32位，除数可以最多可以左移31位
我们尝试让除数从最大的位移（32）开始，向左位移即乘以2 ^ shift，如果位移之后的数字比被除数小，那么证明2的shift幂是一个有效的因数，我们把它累加到结果中，之后被除数减去除数和这个因子的积，即取模
一次类推，逐渐进行直到我们尝试完所有的（0-31，总共32）个因数
'''