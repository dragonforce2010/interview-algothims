'''Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
'''
class Solution:
    def comibnationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.dfs(candidates, target, 0, [])
        return self.result

    def dfs(self, candidates, target, start, valuelist):
        if target == 0:
            self.result.append(valuelist[:])
            return

        if i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                return

            valuelist.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, valuelist)
            valuelist.pop()

'''
算法武器：排序（方便结果去重） + dfs深度优先搜索 + 递归

注意，因为本题的元素可以重复利用，所以在递归的时候，我向下传递的start值还是i，在下层递归函数中依然会考虑加入candidates[i]是否能够满足条件的情形。

# 深搜
self.dfs(candidates, target - candidates[i], i, valuelist)
像这种结果要求返回所有符合要求解的题十有八九都是要利用到递归，而且解题的思路都大同小异
相类似的题目有 Path Sum II 二叉树路径之和之二，Subsets II 子集合之二，Permutations 全排列，Permutations II 全排列之二，Combinations 组合项等等
如果仔细研究这些题目发现都是一个套路，都是需要另写一个递归函数，这里我们新加入三个变量，start记录当前的递归到的下标，out为一个解，res保存所有已经得到的解，每次调用新的递归函数时，此时的target要减去当前数组的的数
'''