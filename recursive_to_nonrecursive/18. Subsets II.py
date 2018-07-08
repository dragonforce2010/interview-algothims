'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Example
Input: [1,2,2]
Output:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
Challenge
Can you do it in both recursively and iteratively?
'''
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    # 递归解法
    def subsetsWithDup1(self, nums):
        # write your code here
        if not nums:
            return [[]]
            
        self.subsets = []
        self.dfs(sorted(nums), [], 0)
        return self.subsets
        
    def dfs(self, nums, subset, startIndex):
        self.subsets.append(subset[:])
        
        for index in range(startIndex, len(nums)):
            if index > startIndex and nums[index] == nums[index - 1]:
                continue
            
            subset.append(nums[index])
            # 注意：这里的第三个参数： index + 1
            # 很多人会不小心写成startIndex + 1，这是不对的
            self.dfs(nums, subset, index + 1)
            subset.pop()
            

    # 非递归解法
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]

        nums.sort()
        results, stack, startIndex = [], [], 0
        stack.append(([], 0))

        while stack:
            subset, startIndex = stack.pop()
            results.append(subset[:])

            for i in range(startIndex, len(nums)):
                if i > startIndex and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                stack.append((subset[:], i + 1))
                subset.pop()

        return results

'''
递归转非递归思路：
- 我们使用一个栈来保存我们在递归时需要用到的局部变量和局部参数，可以让栈的元素是一个元组，这样我们递归中的参数列表就和元组列表非常像
- 非递归的结束条件是栈为空的时候
- 非递归中涉及到的backtracking和递归时很像，只是要记住我们把局部状态加入栈的时候要克隆引用对象，比如如下语句
   stack.append((subset[:], i + 1)) 
'''
