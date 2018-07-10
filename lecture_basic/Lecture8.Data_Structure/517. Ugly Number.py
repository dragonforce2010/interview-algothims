'''
Write a program to check whether a given number is an ugly number`.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Example
Given num = 8 return true
Given num = 14 return false
'''
class Solution:
    def isUgly(self, num):
        if num <= 0:
            return False

        if num == 1:
            return True

        while num >= 2 and num % 2 == 0:
            num /= 2
        while num >= 3 and num % 3 == 0:
            num /= 3
        while num >= 5 and num % 5 == 0:
            num /= 5

        return num == 1
'''
本题学会了对因数的处理技巧。如果我们想要除去某一个数中的某个因数，那么我们的技能就是不断地连续除以这个因数
'''