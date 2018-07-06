'''
Write a function that add two numbers A and B.

Example
Given a=1 and b=2 return 3.

Challenge
Of course you can just return a + b to get accepted. But Can you challenge not do it like that?(You should not use + or any arithmetic operators.)
'''
class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b 
    """
    def aplusb(self, a, b):
        # write your code here
        while b:
            localsum = a ^ b
            carry = (a & b) << 1
            a = localsum
            b = carry
            
        return a
'''
// 主要利用异或运算来完成 
// 异或运算有一个别名叫做：不进位加法
// 那么a ^ b就是a和b相加之后，该进位的地方不进位的结果
// 然后下面考虑哪些地方要进位，自然是a和b里都是1的地方
// a & b就是a和b里都是1的那些位置，a & b << 1 就是进位
// 之后的结果。所以：a + b = (a ^ b) + (a & b << 1)
// 令a' = a ^ b, b' = (a & b) << 1
// 可以知道，这个过程是在模拟加法的运算过程，进位不可能
// 一直持续，所以b最终会变为0。因此重复做上述操作就可以
// 求得a + b的值。
'''