'''Description
Given a string, find the length of the longest substring without repeating characters.
Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

Challenge 
O(n) time
'''

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s:
            return 0
            
        myhash, ans = {}, 0
        start, end = 0, 0
        for start in range(len(s)):
            while end < len(s) and s[end] not in myhash:
                myhash[s[end]] = True
                ans = max(ans, end - start + 1)
                end += 1
                
            del myhash[s[start]]
            
        return ans

'''Summary
算法武器：前向型双指针问题
本题是滑动窗口类问题，要求寻找出满足条件的 # 最大 # 窗口长度。

通用解决策略：
使用两个指针start， end扫描一遍数组，外层为for循环，内存为while循环，while循环内每满足一次条件，就更新答案，接着向前移动end指针

因为内层的while循环并没有回溯，所以整个时间复杂度可以优化到O（n）

本题的start，end，ans变量定义以及for，while循环是一个模板，记住此类写法。

start代表窗口的上届，我们用for循环来枚举窗口上界可以取到的值。end是窗口的下届，我们使用while循环寻找到以当前start作为上届的，能够满足题意要求的窗口下届，然后更新一次答案。
end的指针是一直向前走的，没有回头，即没有回溯，所以整体复杂度就降下来了。

注意：
- 本题求的满足题目条件的上界答案
- 所以在while循环中，我们的条件是end在边界内，同时满足题目的条件（代表当前找到一个解），所以我们就更新一下全局解
'''
