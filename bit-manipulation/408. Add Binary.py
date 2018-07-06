'''
Given two binary strings, return their sum (also a binary string).

Example
a = 11

b = 1

Return 100
'''
class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        indexa = len(a) - 1
        indexb = len(b) - 1
        result = []
        carry = 0
        
        # while循环的条件是只要string a或b其中一个没有扫描完就继续进行
        while indexa >= 0 or indexb >= 0:
            # 如果某个string已经被扫描完了，我们就用0表示其数组
            operanda = int(a[indexa]) if indexa >= 0 else 0
            operandb = int(b[indexb]) if indexb >= 0 else 0
            localResult = (operanda + operandb + carry) % 2
            carry = (operanda + operandb + carry) // 2
            result.append(str(localResult))
            
            # 注意移动指针，使得while循环能够结束
            indexa -= 1
            indexb -= 1

        # 记住在末尾检查进位    
        if carry == 1:
            result.append('1')
            
        # 需要翻转result数组，才能得到正确的表示
        return ''.join(reversed(result))
'''
算法武器：数字逐位相加求和 + carry计算

本题考查string类型的大数相加算法，我们要了解一下基本点

累加需要从最低位开始，也就是从string的最后一位开始
累加结束条件是两个字符串都遍历完毕的时候
每次累加计算的本层计算结果是：
(carry + a + b) % 2
每次累加本层进位结果是：
(carry + a + b) / 2
当while循环跳出时,不要忘记检查最后的进位，如果进位是1，我们需要在结果前补上“1”
'''            
