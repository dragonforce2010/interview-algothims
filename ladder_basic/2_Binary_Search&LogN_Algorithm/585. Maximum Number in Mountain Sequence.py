'''Description
Given a mountain sequence of n integers which increase firstly and then decrease, find the mountain top.

Example
Given nums = [1, 2, 4, 8, 6, 3] return 8
Given nums = [10, 9, 8, 7], return 10
'''
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1
            
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            m1 = (left + right) // 2
            m2 = (m1 + 1 + right) // 2
            if nums[m1] < nums[m2]:
                left = m1 + 1
            elif nums[m1] > nums[m2]:
                right = m2 - 1
            else:
                left = m1 + 1
                right = m2 - 1
                
        return max(nums[left], nums[right])
'''Summary
算法武器：三分法
三分法适合找凸函数的最大值和最小值问题。
三分法和二分法的思路都是一样的，都是通过一有效切分，根据切分点判断，切去解不在的区间，保留解在的区间，将问题的规模缩小，化繁为简。

算法思路：

计算两个指针m1, m2, 这两个指针把数组分成了三段，故命名为三分法
m1 = left + (right - left) / 2
m2 = right - (right - m1) / 2
比较m1和m2的值，决定如何更新left和right的指针，整个while循环的条件是left + 1 < right, 也就是数组中必须至少有三个元素，该while才会进行，while跳出时，我们需要对端点left和right所指向元素进行单独判断
如果m1 > m2, 那么m1更加接近最大值，所以我们可以舍弃整个m2右边的区间（包括m2），把整个问题缩小，即right = m2 - 1
如果m1 < m2, 那么m2更加接近最大值，那么我们可以舍弃整个m1左边的区间（包括m1），把整个问题缩小，即left = m1 + 1
如果m1 == m2, 那么最大值在m1和m2的区间之中（包括m1和m2），把整个问题缩小，即left = m1, right = m2
http://blog.csdn.net/beiyouyu/article/details/7875480
一. 概念
在二分查找的基础上，在右区间（或左区间）再进行一次二分，这样的查找算法称为三分查找，也就是三分法。
三分查找通常用来迅速确定最值。
二分查找所面向的搜索序列的要求是：具有单调性（不一定严格单调）；没有单调性的序列不是使用二分查找。
与二分查找不同的是，三分法所面向的搜索序列的要求是：序列为一个凸性函数。通俗来讲，就是该序列必须有一个最大值（或最小值），在最大值（最小值）的左侧序列，必须满足不严格单调递增（递减），右侧序列必须满足不严格单调递减（递增）。如下图，表示一个有最大值的凸性函数：
二、算法过程
（1）、与二分法类似，先取整个区间的中间值mid。
[cpp] view plain copy
mid = (left + right) / 2;
（2）、再取右侧区间的中间值midmid，从而把区间分为三个小区间。
[cpp] view plain copy
midmid = (mid + right) / 2;
（3）、我们mid比midmid更靠近最值，我们就舍弃右区间，否则我们舍弃左区间？。
比较mid与midmid谁最靠近最值，只需要确定mid所在的函数值与midmid所在的函数值的大小。当最值为最大值时，mid与midmid中较大的那个自然更为靠近最值。最值为最小值时同理。
[cpp] view plain copy
if (cal(mid) > cal(midmid))
right = midmid;
else
left = mid;
（4）、重复（1）（2）（3）直至找到最值。
算法的正确性：
1、mid与midmid在最值的同一侧。由于凸性函数在最大值（最小值）任意一侧都具有单调性，因此，mid与midmid中，更大（小）的那个 数自然更为靠近最值。此时，我们远离最值的那个区间不可能包含最值，因此可以舍弃。
2、mid与midmid在最值的两侧。由于最值在中间的一个区间，因此我们舍弃一个区间后，并不会影响到最值
'''