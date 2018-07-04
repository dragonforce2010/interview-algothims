'''
Find K-th largest element in an array. and N is much larger than k.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.
'''
class Solution:
    # @param nums {int[]} an integer unsorted array
    # @param k {int} an integer from 1 to n
    # @return {int} the kth largest element
    
    
    def kthLargestElement2(self, nums, k):
        # Write your code here
        import heapq
        heap = []
        
        
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heapq.heappop(heap)
'''
算法武器： heap

本题意图实在考堆
相求第k大元素，那么就把数组中元素全部入堆，维持一个size为k的最小堆，该堆pop一下即是第k大元素
之所以维持最小堆的原因是我们堆的size为k，当堆的元素个数大于k时，我们就需要移除一个，这个时候我们希望移除最小的一个，所以我们使用最小堆

堆构建完成之后，堆中的元素是k个最大元素
由于是小根堆，所以堆顶元素就是第k大元素
每当加入一个元素，堆的size改变的时候就检查一下，如果堆中元素超过k时，将最小元素出堆
'''