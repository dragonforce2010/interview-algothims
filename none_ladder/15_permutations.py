'''Description:
Given a list of numbers, return all possible permutations.

Notice
You can assume that there is no duplicate numbers in the list.

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
'''

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        self.results = []
        self.dfs(nums, [])
        return self.results
     
    # 定义：计算nums的全排列，使用seq数组保存局部结果，局部结果集满足一定条件将加入到最终结果集：self.results数组中
    # 遍历nums中的每一个元素，选择一个加入到seq之中，然后递归进行，直到nums数组为空   
    def dfs(self, nums, seq):
        if not nums:
            # 将seq数组复制一份，放到全局结果集中
            self.results.append(seq[:])
            return
        
        for i in range(len(nums)):
            ele = nums.pop(i)
            seq.append(ele)
            self.dfs(nums, seq)
            # 回溯过程，非常重要
            seq.pop()
            nums.insert(i, ele)


'''Summary
算法武器：排序（方便去重） + dfs深度优先搜索 + 递归
这道题目和subset的解题过程很类似，都是对于一个给定的nums集合，我们用for循环遍历一遍nums，对于每个遍历到的元素，我们都尝试将其加入到局部解中或者不加入局部解。两道题输出的解的个数都是相同的，都是2^n.
只不过两题使用的缩小递归子问题的规模的方式不同。subsets使用startIndex控制传入数组的有效作用范围，本题是直接传入一个更小的数组到子递归函数中，所以回溯也略有不同。
'''
