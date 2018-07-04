'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Example
For [4, 5, 1, 2, 3] and target=1, return 2.

For [4, 5, 1, 2, 3] and target=0, return -1.

Challenge
O(logN) time
'''
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        
        if not A:
            return -1
            
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
                
            # 通过start和mid处元素的值，我们推知我们的mid中线处在哪个图形段中（如果画图可以看到有两端）
            if A[start] < A[mid]: 
                # 我们我们确定target在start和mid之间，我们则可以放心地更新end
                if A[start] <= target and target <= A[mid]: 
                    end = mid
                # 否则我们排除start左边的解空间
                else:
                    start = mid
            else: 
                if A[mid] <= target and target <= A[end]: 
                    start = mid
                else:
                    end = mid
        
        if A[start] == target:
            return start
        if A[end] == target:
            return end
            
        return -1
        
    # def search(self, A, target):
    #     # write your code here
        
    #     if not A:
    #         return -1
            
    #     start, end = 0, len(A) - 1
    #     while start + 1 < end:
    #         mid = start + (end - start) / 2
    #         if A[mid] == target:
    #             return mid
                
    #         if A[start] <= target and target <= A[mid]: 
    #             end = mid
    #         else:
    #             start = mid
    #         else: 
    #             if A[mid] <= target and target <= A[end]: 
    #                 start = mid
    #             else:
    #                 end = mid
        
    #     if A[start] == target:
    #         return start
    #     if A[end] == target:
    #         return end
            
    #     return -1