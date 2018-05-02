'''Description
Find K-th largest element in an array.
Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

Challenge 
O(n) time, O(1) extra memory.
'''

import heapq
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    # def kthLargestElement(self, k, A):
    #     import heapq
    #     heapq.heapify(A)
    #     return heapq.nlargest(k, A)[-1]
        
        
    def kthLargestElement(self, k, A):
        if not A or k < 0:
            raise Exception('Invalid parameter!')
            
        heap = []
        for elem in A:
            heapq.heappush(heap, elem)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heap[0]
'''Summary
算法武器：堆
'''

