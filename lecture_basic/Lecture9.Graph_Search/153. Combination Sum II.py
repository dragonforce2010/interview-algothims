'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]
'''
class Solution:
    def combinationSum2(self, candidates, target):
        self.result = []
        self.dfs(sorted(candidates), target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, valuelist):
        if target == 0:
            self.result.append(valuelist[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                return
            
            valuelist.append(candidate[i])
            self.dfs(candidates, target - candidates[i], i + 1, valuelist)
            valuelist.pop()