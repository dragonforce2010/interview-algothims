'''Description
There is an integer array which has the following features:
The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:

A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

 Notice
It's guaranteed the array has at least one peak.
The array may contain multiple peeks, find any of them.
The array has at least 3 numbers in it.
Example
Given [1, 2, 1, 3, 4, 5, 7, 6]

Return index 1 (which is number 2) or 6 (which is number 7)
'''
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        
        if not A or len(A) < 3:
            return 0
            
        start, end = 1, len(A) - 2
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]:
                start = mid
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            # else:
            #     start = mid
                
        return end if A[start] < A[end] else start
'''
算法武器：二分法
算法思想：
- 二分法并不一定是要用在单调序列上的，只要我们有一个二分的思路，并且根据这个思路，我们总能砍去解不在的空间，保留解存在的空间，以缩小问题的规模，那么我们就可以使用二分法
- 本题二分法的判断依据是更具数学中f'(a)*f'(b) < 0 => a和b之间存在极值点，如果a到b先升后降，那么a，b之间存在极大值

注意：
本题要求找到一个山峰，一个峰的构成至少有三个元素，而且肯定不在首尾，所以我们在初始化start和end时候用如下值：

start, end = 1, len(A) - 2
这样的初始化就不会让我们的程序有任何越界的风险了
'''