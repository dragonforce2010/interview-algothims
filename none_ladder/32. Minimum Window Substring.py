'''
Given a string source and a string target, find the minimum window in source which will contain all the characters in target.

Example
For source = "ADOBECODEBANC", target = "ABC", the minimum window is "BANC"

Challenge
Can you do it in time complexity O(n) ?
'''
from collections import defaultdict
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if source is None or target is None:
            return None
        
        if not source or not target:
            return ""
        
        start, end = 0, 0    
        minimumLength, ansl, ansr = 290910291, 0, 0
        windowSubstring = ""
        sourceHashmap = defaultdict(int)
        targetHashmap = defaultdict(int)
        
        for ch in target:
            targetHashmap[ch] += 1
            
        for start in range(len(source)):
            # 注意：while循环判断isSourceHashMapContainsTarget在先，然后才把end所指向的元素加入到sourcehash中，该sourcehash会在下一次
            # 进行判断，所以end所指向的位置总是比当前sourcehash中的元素超前一步
            while end < len(source) and not self.isSourceHashMapContainsTarget(sourceHashmap, targetHashmap):
                print(start, end, source[end])
                sourceHashmap[source[end]] += 1
                end += 1
                # print('end:', end)
                
            
            # 在这里，不论是1）end >= len(source)而退出循环，还是2）isSourceHashMapContainsTarget失败而退出循环
            # 我们都需要再次检查条件，看看是否满足要求，并且如果满足要求，我们的窗口长度计算公式总是end - start
            # 因为不论原因1或者2，致使退出，end都指向一个不应被包括的端点    
            if self.isSourceHashMapContainsTarget(sourceHashmap, targetHashmap) and end - start < minimumLength:
                minimumLength = end - start
                windowSubstring = source[start:end]
                # print(start, end)
                # print("result:", windowSubstring)
            
            sourceHashmap[source[start]] -= 1
            if sourceHashmap[source[start]] == 0:
                del sourceHashmap[source[start]]
        
        return windowSubstring
        
        
    def isSourceHashMapContainsTarget(self, sourceHashmap, targetHashmap):
        for ch in targetHashmap:
            if sourceHashmap[ch] < targetHashmap[ch]:
                return False
          
        return True