'''
Given a list of numbers, return all possible permutations.

Example
For nums = [1,2,3], the permutations are:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Challenge
Do it without recursion.
'''
class Solution:
    def permute(self, nums):
        if nums is None:
            return []

        self.result = []
        self.dfs(sorted(nums), [])
        return self.result

    def dfs(self, nums, seq):
        if not nums:
            self.result.append(seq[:])
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seq.append(nums[i])
            nums.pop(i) # delete element at index i
            self.dfs(nums, seq)
            nums.insert(i, nums[i]) # insert element at index i
            seq.pop()
'''
算法武器：排序（方便去重） + dfs深度优先搜索 + 递归

这道题目和subset的解题过程很类似，都是对于一个给定的nums集合，我们用for循环遍历一遍nums，对于每个遍历到的元素，我们都尝试将其加入到局部解中或者不加入局部解。两道题输出的解的个数都是相同的，都是2^n.
只不过两题使用的缩小递归子问题的规模的方式不同。subsets使用startIndex控制传入数组的有效作用范围，本题是直接传入一个更小的数组到子递归函数中，所以回溯也略有不同。
'''