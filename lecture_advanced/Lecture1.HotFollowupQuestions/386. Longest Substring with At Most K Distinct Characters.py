'''
Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.

Challenge
O(n), n is the size of the string s.
'''
import collections
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k <= 0:
            return 0
            
        start, end, ans = 0, 0, 0
        myhash = collections.defaultdict(int)
        for start in range(len(s)):
            while end < len(s):
                myhash[s[end]] += 1
                if len(myhash) <= k:
                    end += 1
                else:
                    break
                
            ans = max(ans, end -  start)
            
            myhash[s[start]] -= 1
            if myhash[s[start]] == 0:
                del myhash[s[start]]
                
        return ans
'''
算法武器：前向型移窗口类动双指针

本题的题型是滑动窗口类型，使用模板写法：

定义start，end，ans三个变量
start做外层for循环
end做内层while循环
while条件为end的边界和题目的约束
更新答案部分必须要加条件判断
更新答案必须在更新end变量之前
对于hash表的处理都是放在while循环内进行，一般不需要在for层做任何特别处理
注意：

本题求解的是上界答案问题
我们的答案直接在内层while循环中更新，而不需要当while退出之后再根据条件更新答案，因为while循环的条件是end在边界内，同时满足题目条件，这意味着我们找到一组有效解，我们需要和全局解比较，不断更新上界的解
在更新答案的时候还是要确定一下条件，再更新
			if len(hashmap) <= k:
                    ans = max(ans, end - start + 1)
其他类求下界问题，比如sum类求下界问题，我们就需要在跳出while循环单独更新。因为while循环进行的条件是end在边界内，同时不满足条件的时候，我们继续扩大窗口边界，移动end指针。当循环跳出时，我们可能找到了一组有效解，所以我们还需要检查条件是否满足，满足时才将其和全局答案比较、更新
'''