'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
'''
class Solution:
    def combinationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, valuelist):
        if target == 0:
            self.result.append(valuelist[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if target < candidates[i]:
                return

            valuelist.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, valuelist)
            valuelist.pop()
