'''
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose three edges length is the three numbers that we find?

Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
'''
class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        if not S or len(S) < 3:
            return 0
        
        S.sort()
        left, right = 0, len(S) - 1
        ans = 0
        
        for index in range(2, len(S)):
            longestEdge = S[index]
            left, right = 0, index - 1
            while left < right:
                if S[left] + S[right] > longestEdge:
                    ans += right -  left
                    right -= 1
                else: 
                    left += 1
        return ans

'''
算法武器：排序 + 双指针（对冲型）

备注：寻找twosum > target的升级版，本题的target是三角形的斜边，这个斜边可以是数组中的任何一个边，所以我们需要枚举出这个斜边（用一个for循环），内层就变成了twosum > target问题

确定能够构成一个三角形的条件是：两边之和大于第三边

本题中的第一个for循环时遍历第三条边的所有可能值，内层循环是一个two sum问题，two sum的区间从【0，index - 1】
two sum的经典解法就是使用一个while循环，让后左右指针相向而行，通过左右指针所指元素和与target进行比较，确定更新指针的方式。
two sum中，当条件满足时更新答案
'''