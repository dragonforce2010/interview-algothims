'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

Example
Given nums = [2, 7, 11, 15], target = 9
return [1, 2]
'''
class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here
        if not nums:
            return []
            
        l, r = 0, len(nums) - 1
        while l < r:
            value = nums[l] + nums[r]
            if value > target:
                r -= 1
            elif value < target:
                l += 1
            else:
                return[l + 1, r + 1]
        
        return []

'''
算法武器：双指针

算法过程：

定义双指针分别指向数组最左和最右
两个指针所指元素加和
如果和大于目标，那么更新上界，right -= 1
如果和小于目标，那么更新下界，left += 1
如果和定于目标，那么返回结果
注意while循环的条件是 l < r
l = r是不可行的，因为two sum要求是两个数。
'''