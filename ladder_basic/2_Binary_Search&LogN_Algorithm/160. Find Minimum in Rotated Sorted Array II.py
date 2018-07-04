'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Given [4,4,5,6,7,0,1,2] return 0.
'''
class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    
    # solution1
    def findMin(self, num):
        if not num:
            return -sys.maxint
            
        start, end = 0, len(num) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if num[mid] > num[end]:
                start = mid + 1
                # start = mid + 1 ？# This also works fine.
            elif num[mid] < num[end]:
                end = mid - 1
                # end = mid  # This also works fine
            else:
                end = end - 1
                
        return min(num[start], num[end])

'''
算法武器：二分法(基于有重复元素的RSA)

算法思想：

使用二分法模板，定义start，end指针
while循环条件为start < end
while循环体中计算mid，根据mid指向的元素的值和end指向元素的值得关系，有条件地更新start和end指针
当num[mid] > num[end]时，通过画图，我们知道，我们的解在右边，所以我们更新start = mid + 1
当num[mid] < num[end]时，通过画图，我们知道，我们的解在左边，所以我们更新end = mid - 1
当num[mid] == num[end]时，通过画图，我们知道，我们需要进一步缩小上届，因为题目中有重复元素，重复元素会导致死循环,这一步相当关键
本题的解为start和end所指元素中比较小的那个
本题的难点在于想到使用num[mid]和num[end]的关系来最终求解最小值的位置
思路上有点像三分法：

如果mid更接近最小值，那么我们就舍弃end右边部分的区间
如果end更接近最小值，我们就舍弃mid左边的区间（包括mid）
'''