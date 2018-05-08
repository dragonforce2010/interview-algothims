'''Description
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
Example
Given the string = "abcdzdcab", return "cdzdc".

Challenge 
O(n2) time is acceptable. Can you do it in O(n) time.
'''
class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)
        # scan all the possible center pos of palindromic substring
        # i represents the center pos
        for i in range(length * 2):
            if i & 1 : # if i is an odd number
                left = i / 2
                right = left
            else : # if i is an even number
                left = i / 2 - 1
                right = left + 1
            # find the longlest prlindromic substring whose center is s[i]    
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left + 1 > maxx:
                maxx = right - left + 1
                ansl = left
                ansr = right
        return s[ansl: ansr + 1]
                
'''Summary
这题就是一个比较暴力的算法，时间复杂度O(N^2)，枚举中点，然后向两边枚举，判断是否是回文串。
只是Solution是一种比较取巧的方法，原本我们需要考虑回文串长度是奇数还是偶数，但是我们在每个字母中间插入一个#符号。
比如 abcaba =>#a#b#c#a#b#a#, 这样我们去枚举的时候，就不需要考虑奇偶性了，#a#b#a# 这样长度的一半7/2 就是回文串的长度。当然我们的#不是真的去加上，而是出现在我们的想想当中。所以枚举i位置上的字母对应实际位置上的i/2位置上的字母。
'''