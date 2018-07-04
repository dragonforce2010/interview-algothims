'''
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
'''
class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # Write your code here
        hash = {}
        for index, num in enumerate(nums):
            if num + target in hash:
                return sorted([index + 1, hash[num + target] + 1])
            elif num - target in hash:
                return sorted([index + 1, hash[num - target] + 1])
            else:
                hash[num] = index
                
        return []
        
        
        
    # def twoSum7(self, nums, target):
    #     # Write your code here
    #     if not nums or len(nums) < 2:
    #         return []
            
    #     nums.sort()
    #     l, r = 0, len(nums) - 1
        
    #     while l < r:
    #         diff = nums[r] - nums[l]
    #         ......
                
    #     return []
'''
算法武器：哈希表 + 一次数组扫描

由于本题的求两个元素的差值是否为给定target，所有可能有以下关系：

num1 - num2 = target => num1 - target = num2
num2 - num1 = target => num1 + target = num2
我们就根据这两个式子和哈希表求解此问题。
我们扫描遍历数组时，对于每一个遍历到的当前元素，我们使用上述两个式子计算另一个元素，并检查其是否在hash表中，如果在我们就返回答案
'''