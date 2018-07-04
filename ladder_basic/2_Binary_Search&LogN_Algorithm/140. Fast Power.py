'''Description
Calculate the an % b where a, b and n are all 32bit integers.

Example
For 231 % 3 = 2

For 1001000 % 1000 = 0

Challenge
O(logn)
'''

class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    '''
    本题使用了递归思想，递归思想也是一种降维思想，把问题的维度规模降低，直至最简单情形
    很明显，本题的n是在控制问题的维度
    '''
    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        elif n == 0:
            # do not use `1` instead `1 % b` because `b = 1`
            return 1 % b
        elif n < 0:
            return -1

        # (a * b) % p = ((a % p) * (b % p)) % p
        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        
        # 如果n是奇数，我们就少乘了一次n，所以我们要再乘一次a
        if n % 2 == 1:
            product = (product * a) % b

        return product
'''Summary
题解

数学题，考察整数求模的一些特性，不知道这个特性的话此题一时半会解不出来，本题中利用的关键特性为：

(a * b) % p = ((a % p) * (b % p)) % p
即 a 与 b 的乘积模 p 的值等于 a, b 分别模 p 相乘后再模 p 的值，只能帮你到这儿了，不看以下的答案先想想知道此关系后如何解这道题。

首先不太可能先把 ana^nan 具体值求出来，太大了... 所以利用以上求模公式，可以改写 ana^nan 为：

an=an/2⋅an/2=an/4⋅an/4⋅an/4⋅an/4⋅=...a^n = a^{n/2} \cdot a^{n/2} = a^{n/4} \cdot a^{n/4} \cdot a^{n/4} \cdot a^{n/4} \cdot = ...an=an/2⋅an/2=an/4⋅an/4⋅an/4⋅an/4⋅=...

至此递归模型建立。
'''