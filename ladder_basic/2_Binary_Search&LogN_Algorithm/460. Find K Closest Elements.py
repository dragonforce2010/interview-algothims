'''Description
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
'''
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or k > len(A):
            return []
            
        index = self.firstIndexOf(A, target)
        left, right = index - 1,index
        
        result = []
        for i in range(k):
            if left < 0:
                result.append(A[right])
                right += 1
            elif right > len(A) - 1:
                result.append(A[left])
                left -= 1
            else:
                if abs(target - A[left]) <= abs(A[right] - target):
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
                    
        return result
        
    def firstIndexOf(self, A, target):
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
                
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        
        return len(A) - 1
'''Summary
算法武器：二分法 + 双指针（从中间开始，反方向行走）

首先利用二分法找到第一个大于等于target的index
从这个index开始利用双指针向两边搜索，将左右指针指向的差的绝对值较小的放入到结果集中
for循环用于控制向结果集中放多少个元素
for循环内的判断条件解释：
首先检查left指针的有效性，如无效就将right所指元素加入
然后判断right指针的有效性，如果无效就将left所指元素加入
如果left，right都有效，那么就比较谁和target的差比较小，较小的加入到结果集
注意：

3个if条件是互斥的，任何时候只有一个成立，所以这几个条件无所谓先后顺序
我们首先找到了一个index， index = firstIndexOfTarget,然后从这个点开始考察，逐一找到KClosest numbers。要知道这个index的值只是一个开始计算的起始值，并不是唯一的，即使你把它换成lastIndexOf，结果还是一样的。不论从firstIndex还是lastIndex开始，我们都能得到正确答案，因为从这个开始值起，我们会查看left、right指针是否有效，如果都有效，我们总是选择更近的，如果left失效，我们只能选择加入right指针所指元素，同理，如果right失效，我们也只能加入left指针所指元素。总之，这个其实值只是一个方便计算的开始点，它不是唯一的。
注意：
初始化left，right指针时，我们必须初始化为以下：

left, right = index - 1, index
因为index所指元素 >= target, 所以left指针必须初始化成index - 1，这样才能保证答案的正确性。即使我们使用index = lastIndex作为初值，我们的初始化也是上面的形式，即left = index - 1
'''