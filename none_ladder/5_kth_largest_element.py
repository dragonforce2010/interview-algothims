'''Description:
Find K-th largest element in an array.

Notice
You can swap elements in the array
'''


import heapq

class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if k <= 0:
            raise Exception('Invalid parameter! k should be > 0')
            
        heap = []
        for ele in A:
            heapq.heappush(heap, ele)
            if len(heap) > k:
                heapq.heappop(heap)
                
        
        return heapq.heappop(heap) #return heap[0]