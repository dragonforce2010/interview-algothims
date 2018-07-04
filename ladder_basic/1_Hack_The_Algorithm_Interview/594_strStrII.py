'''
Description
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.
'''
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1
            
        if not target:
            return 0
            
        m, n = len(source), len(target)
        sourcehash, targethash, base = 0, 0, 10 ** 6
        
        for i in range(n):
            targethash = (targethash * 31 + ord(target[i])) % base
            
        for i in range(m):
            sourcehash = (sourcehash * 31 + ord(source[i])) % base
            if i < n - 1:
                continue
            
            if i > n - 1:
                sourcehash = (sourcehash - ord(source[i - n]) * 31 ** n) % base
                
            if sourcehash == targethash and source[i - n + 1: i + 1] == target:
                return i - n + 1
                
        return -1
'''Summary
算法武器： rabinKarp (transfer string to hashcode of integer type)
时间复杂度: O(m) + O(n)

思路：
用哈希函数将字符串转化为整型哈希码，将字符串的比较转化为整数的比较，将需要逐个字符串比较的O(目标串的长度)转化为O（1）常数级的整数之间的比较
注意：
既然是哈希，我们一定要有一个哈希空间，本题中我们使用1000000这个整数空间。既然哈希的空间是有限的，那么哈希码可能会产生冲突，所以当两个字符串的哈希码相等时，并不能一定保证两个串相等，所以我们还得二次比较一下，用字符串的比较，这样就万无一失了。
'''