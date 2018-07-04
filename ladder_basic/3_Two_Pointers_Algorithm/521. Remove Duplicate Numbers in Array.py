'''
Given an array of integers, remove the duplicate numbers in it.

You should:

Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
Example
Given nums = [1,3,1,4,4,2], you should:

Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.

Challenge
Do it in O(n) time complexity.
Do it in O(nlogn) time without extra space.
'''
class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        # 
        if not nums:
            return 0
            
        cursor = 0
        nums.sort()
        for num in nums:
            if num != nums[cursor]:
                nums[cursor + 1] = num
                cursor += 1
        
        return cursor + 1
'''
算法武器：数组单指针 + 一遍扫描

算法思路：
-先对nums数组进行排序，因为我们需要相同数连起来

使用单指针cursor指向数组中不重复元素的最后一个位置
使用for循环扫描每个元素
如果扫描到的元素和cursor所指元素不同，那么我们就将该元素复制到cursor + 1的位置，然后cursor = cursor + 1，使cursor始终指向数组中不重复元素的最后一个位置
算法结束时返回cursor + 1
注意：最后返回的是元素的个数，所以我们要把cursor + 1
'''