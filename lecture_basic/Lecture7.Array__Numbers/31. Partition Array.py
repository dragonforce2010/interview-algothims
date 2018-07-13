'''
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge
Can you partition the array in-place and in O(n)?
'''
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0
            
        left, right = 0, len(nums) - 1
        '''
        partition array 没有快排那么严格，要求对于nums[i] == k的元素进行均匀分布，而是将等于k的元素统一放在右边，
        所以我们的三个while循环中，我们的left < right即可
        '''
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            
            '''这里有个等于'''    
            while left < right and nums[right] >= k:
                right -= 1
                
            '''在进行交换的时候需要判断left < right'''
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        '''
        返回答案的时候，需要判断nums[left]是否小于k
        要考虑到几种特殊的输入情形：
        1.k < min(nums), so when algorithm ends, then
          left = 0, right = 0
          ans: left
        2.k > max(nums) so when algorithm ends, then
          left = len(nums) - 1, right = len(nums) - 1
          ans: left + 1
        3.min(nums) < k < max(nums) so when algorithm ends, then
          left > right
          ans: left
        '''        
        return left + 1 if nums[left] < k else left
        
            
