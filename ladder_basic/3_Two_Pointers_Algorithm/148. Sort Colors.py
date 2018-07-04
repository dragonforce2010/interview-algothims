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
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        # makes all the zeros in position, the returned index is the pos after last 0 in the array
        # for exmple: 
        # input: [1,1,0,2,1,1,1,2,0,1,0,0,2,0,2,1,1,0,0,0,0,2,0,2,0,1,2,2]
        # output:[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2]
        # index: 11
        index = self.sort(A, 0, 0)
        # print(A, index)
        
        # makes all the 1s in position
        # output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
        self.sort(A, 1, index) 
        # print(A)
    
    # make all the elems which equals to target in array A[index:] in position(left part of the array)
    def sort(self, A, target, index):
        start, end = index, len(A) - 1
        while start <= end:
            while start <= end and A[start] == target:
                start += 1
            while start <= end and A[end] != target:
                end -= 1
            if start <  end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            # print(",".join([str(i) for i in A]), start, end)
        return start
'''
算法武器：双指针

题型：数组按序划分

算法思路：

将数组中的元素分成两类，一类等于target，一类不等于target
首先将数组中的元素0进行归位，方法和partition思想类似，算法结束后，0在数组最左边，非0在数组最右边
然后将数组中的1元素进行归位，归位的开始节点index是前一步中返回的index，即数组中首个非0元素的位置。算法结束后1元素归位，剩下的就自然是2元素了。
还有一种解法可供参考
算法武器：三指针
问题：为什么mid和left交换之后，mid也需要+1？
答案：因为mid的指针永远比left走得快，而mid走过的地方一定都是1，所以当mid和left交换时，交换过来的元素一定是1，所以我们无需判断这个元素，可以在++left同时++mid
思路：
本题使用3指针解法，因为题目要求把color分成3类。

第一个指针left从最左边0开始走，方向向右，left走过的元素都为0
第二个指针right从右len(A) - 1向左走，方向向左，right走过的元素都为2
第三个指针mid，mid的初始化为第一个不为0的位置，mid方向向右，边界是right指针即mid <= right
算法过程：
初始化left，用while循环找到第一个第一个left指向元素不为0的位置
初始化right，用while循环找到第一个right指向元素不为0的位置
初始化mid， mid = left，用while循环遍历 mid: left -> right的范围
遇到0就把A[mid]和A[left]交换，更新left和mid
遇到2就把A[mid]和A[right]交换， 更新right
遇到1就把mid指针右移
注意：本题中的下面这个代码块其实也可以注释掉
while left < right and A[left] == 0:
left += 1
while left < right and A[right] == 2:
right -= 1
'''