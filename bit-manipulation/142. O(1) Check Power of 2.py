'''
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;

For n=5, return false;

Challenge
O(1) time
'''
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n < 1:
            return False
            
        return n & (n - 1) == 0

'''
用O(1)的时间检查一个数是否是2的平方。这里可以用位运算。我们可以先列举一下，2的倍数的二进制数分别是10、100、1000、10000、100000等等。找到规律后，可以发现
符合这种规律的数都是最左边是一个1，然后右边都是0.那我们把它减去1之后再看看，分别是01、011、0111、01111、011111等等。然后再把他两做&操作，发现得到的都是0了。这个规律是肯定成立的，利用这个规律就可以在O(1)时间内判断了：
'''