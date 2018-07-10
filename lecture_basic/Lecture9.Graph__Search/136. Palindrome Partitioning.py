'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s):
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s, stringlist):
        if not s:
            self.res.append(stringlist[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                stringlist.append(s[:i])
                self.dfs(s[i:], stringlist)
                stringlist.pop()

    def isPalindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - 1 - i]:
                return False

        return True