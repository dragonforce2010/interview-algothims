'''Description:
Given a list of numbers with duplicate number in it. Find all unique permutations.

'''
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        self.result = []
        # 排序非常重要，这是去重的重要准备环节
        self.dfs(sorted(nums), [])
        return self.result
        
    
    # 计算nums数组的全排列，将局部结果保存在seq中，将符合条件的结果放入全局结果集：self.result
    def dfs(self, nums, seq):
        if not nums:
            self.result.append(seq[:])
            return
        
        for i in range(len(nums)):
            # 去重，如果当前元素和上一个元素一样，那么生成的排列也是相同的，所以需要跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            ele = nums.pop(i)
            seq.append(ele)
            self.dfs(nums, seq)
            # 回溯
            seq.pop()
            nums.insert(i, ele)
            
'''Summary
算法武器：排序（方便去重） + dfs深度优先搜索 + 递归

注意：
- 本题的排列是和顺序有相关性的，不同的顺序有不同的结果，所以我们在本题中不能使用如同comination sum那种方式使用startIndex去控制子问题规模。
- 因为在combination sum中，我们要求排序，要求自问题不能再使用以前处理过的元素，确切讲不能使用在该元素之前的元素(排序的)，这显然不适用于排列
- 所以排列使用的是通过传入更小的子集来缩小问题的规模
- 本题排列的思想是：对于给定的集合，我们选取任意一个元素（选取的方法有很多种，我们使用dfs来做），将其加入局部解，然后把剩下的子集进行递归调用，直到传入子集为空时，dfs退出。

这道题目和subset的解题过程很类似，都是对于一个给定的nums集合，我们用for循环遍历一遍nums，对于每个遍历到的元素，我们都尝试将其加入到局部解中或者不加入局部解。两道题输出的解的个数都是相同的，都是2^n.

只不过两题使用的缩小递归子问题的规模的方式不同。subsets使用startIndex控制传入数组的有效作用范围，本题是直接传入一个更小的数组到子递归函数中，所以回溯也略有不同。
'''