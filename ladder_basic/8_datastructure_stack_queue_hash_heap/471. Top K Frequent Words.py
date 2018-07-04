'''
Given a list of words and an integer k, return the top k frequent words in the list.

Example
Given

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],

Challenge
Do it in O(nlogk) time and O(n) extra space.
'''
from collections import *
class Solution:
    # @param {string[]} words a list of string
    # @param {int} k an integer
    # @return {string[]} a list of string
    def topKFrequentWords(self, words, k):
        # Write your code here
        dict = defaultdict(int)
        for word in words:
            dict[word] += 1
        p = []
        for key, value in dict.items():
            p.append((value, key))

        p.sort(cmp=self.cmp)
        
        result = []
        for i in xrange(k):
            result.append(p[i][1])
        return result

    def cmp(self, a, b):
        if a[0] > b[0] or a[0] == b[0] and a[1] < b[1]:
            return -1
        elif a[0] == b[0] and a[1] == b[1]:
            return 0
        else:
            return 1

'''
算法武器：哈希表统计 + 排序

题目中需要对结果进行特殊排序，所以我们写了一个专门的cmp函数作为排序的依据
'''