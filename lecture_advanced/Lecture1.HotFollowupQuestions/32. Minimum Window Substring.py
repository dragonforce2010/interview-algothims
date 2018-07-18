'''
Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

Example
For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"

Challenge
Can you do it in time complexity O(n) ?
'''
from collections import defaultdict

class Solution:
    def minWindow(self, source, target):
        if source is None or target is None:
            return None

        if not source or not target:
            return ""

        start, end = 0, 0
        minimumLength, windowSubstring = sys.maxsize, ""
        sourceHashmap, targetHashmap = defaultdict(int), defaultdict(int)

        for ch in target:
            targetHashmap[ch] += 1

        for start in range(len(source)):
            while end < len(source) and not self.isSourceHashMapContainsTarget(sourceHashmap, targetHashmap):
                sourceHashmap[source[end]] += 1
                end += 1

            if self.isSourceHashMapContainsTarget(sourceHashmap, targetHashmap) and end - start < minimumLength:
                minimumLength = end - start
                windowSubstring = source[start:end]

            sourceHashmap[source[start]] -= 1
            if sourceHashmap[source[start]] == 0:
                del sourceHashmap[source[start]]

        return windowSubstring