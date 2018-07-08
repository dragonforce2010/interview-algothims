'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
'''
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum1(self, candidates, target):
        # write your code here
        if not candidates:
            return []
            
        candidates.sort()
        self.result = []
        self.dfs(candidates, target, [], 0)
        
        return self.result
        
    def dfs(self, candidates, target, combs, startIndex):
        if startIndex > len(candidates) - 1:
            return
        
        if target == 0:
            self.result.append(combs[:])
            return

        for index in range(startIndex, len(candidates)):
            if index > startIndex and candidates[index] == candidates[index - 1]:
                continue
            
            if candidates[index] > target:
                break
            
            combs.append(candidates[index])
            self.dfs(candidates, target - candidates[index], combs, index)
            combs.pop()
            
    # non-recursive Solution
    '''
    - 非递归解法使用栈这种数据结构实现
    - 栈中保存的东西是一个元组，这个元组的内容和我们递归解法的参数列表是一样的
    - 非递归的框架是while栈不为空时，不断地从栈中pop出搜索节点，然后处理该节点，逻辑大致和递归相同
    - 非递归处理逻辑中，把递归中的return的地方变成了continue，表示skip这种状态，这是和递归方法的一个不同之处
    '''
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
            
        candidates.sort()
        result, stack = [], []
        stack.append((target, [], 0))
        
        while stack:
            target, combs, startIndex = stack.pop()
            if startIndex > len(candidates) - 1:
                continue
            
            if target == 0:
                result.append(combs)
                continue
            
            for index in range(startIndex, len(candidates)):
                if index > startIndex and candidates[index] == candidates[index - 1]:
                    continue
                
                if candidates[index] > target:
                    break
                
                combs.append(candidates[index])
                stack.append((target - candidates[index], combs[:], index))
                combs.pop()
                
        return result