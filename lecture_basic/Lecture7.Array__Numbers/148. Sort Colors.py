'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return
        
        
        '''
        一遍扫描数组，使用两个边界指针和一个游标指针
        边界指针用于确定边界范围
        - pl指针用于表示[0, pl）之间的元素都为0
        - pr指针用于表示(pr, len(nums) - 1]之间的元素为2
        - cur游标指针表示从[pl, cur）之间的元素为1
        这样两个边界指针和一个游标指针就把整个数组区域分成了3个部分
        '''
        pl, cur, pr = 0, 0, len(nums) - 1
        
        '''
        注意这里的结束条件是cur <= pr,因为pr所指的元素没有被探索过，是不确定的，需要用游标能够遍历到
        pr右侧的部分是确定的，一定是2的元素区域
        '''
        while cur <= pr:
            if nums[cur] == 0:
                nums[cur], nums[pl] = nums[pl], nums[cur]
                pl += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[pr] = nums[pr], nums[cur]
                pr -= 1