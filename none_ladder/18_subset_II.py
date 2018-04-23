'''Description:
Given a list of numbers that may has duplicate numbers, return all possible subsets
Notice
Each element in a subset must be in non-descending order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        self.subsets = []
        self.dfs(sorted(nums), [], 0)
        return self.subsets
    
    # 求出nums数组中[startIndex:]这部分的所有子集，并把他们加入到全局结果    
    def dfs(self, nums, subset, startIndex):
        # 这里一定要把subset的克隆加入到结果集，而不是subset引用，否则结果会错误
        self.subsets.append(subset[:])
        
        for index in range(startIndex, len(nums)):
            # 这里条件是index > startIndex，不是index > 0
            if index > startIndex and nums[index] == nums[index - 1]:
                continue
            
            subset.append(nums[index])
            # 注意这里是index + 1， 不是startIndex + 1
            self.dfs(nums, subset, index + 1)
            subset.pop()

'''Summary
算法武器：排序（以方便我们去重） + dfs深度优先遍历+递归

本题和combination sum的题目类似，都是要求解出所有的子集，对于combination sum，还进一步要求在子集中过滤符合条件的解（元素和等于给定target），然后才能将其加入全局解。而本题仅要求求解所有子集，所以比较简单。当然在求解过程中，我们都需要对自己进行去重操作，为了有效去重，我们必须保证给定的输入是经过排序的。

求解子集的过程:
遍历给定集合中的每一个元素，每一个元素都可以选择加入子集或者不加入子集，然后由此进行递归，递归调用结束之后，我们需要进行回溯。
subsets这道题目是首先将当前局部subset集合加入解集得，然后尝试构造新的解，缩小问题规模，进一步递归调用。

dfs函数的定义是递归的：在给定的集合中按序选择一个元素尝试将其加入到局部变量/局部子集subset中（本次尝试结束之后需要回溯），然后递归调用自己，在剩下的集合中（这是一个规模更小的集合，集合尺寸被startIndex限定），做相同的事情，直到做完所有的尝试。

dfs就是对解决问题的当前步骤做各种尝试，每种尝试都会缩小问题的规模，解决问题的一小部分，每种尝试都是一次递归，每种递归都会产生一颗搜索子树，子树中包含很多可能的解。每个递归都会查看是否局部解已经满足条件，进而将其加入全局解。
'''
