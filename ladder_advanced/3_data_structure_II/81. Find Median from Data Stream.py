'''Description
Numbers keep coming, return the median of numbers at every time a new number added.
Clarification
What's the definition of Median?
- Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

Challenge 
Total run time in O(nlogn).
'''
import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    
    minHeap, maxHeap = [], []
    # maintains the total counts of the heap
    numbers = 0
    def medianII(self, nums):
        ans = []
        # scan the nums and push each element to the heap(maxHeap and minHeap)
        # calculate median and put it into the ans
        for item in nums:
            self.add(item)
            ans.append(self.getMedian())
        return ans
        
    # The top element in maxHeap is the ans
    def getMedian(self):
        return -self.maxHeap[0]

    def add(self, value):
        # if current numbers is even, then put element in maxHeap
        # note: maxHeap is on the left, minHeap is on the right
        # elements in maxHeap should be less than elements in minHeap
        if self.numbers % 2 == 0:
            # we put negative value to maxHeap array to make it a max heap
            heapq.heappush(self.maxHeap, -value)
        else:
            heapq.heappush(self.minHeap, value)
        self.numbers += 1
        
        # if maxHeap and minHeap have at least one element, then we need to main the top element of both heap
        # note: maxHeap is on the left, minHeap is on the right
        # elements in maxHeap should be less than elements in minHeap
        if len(self.minHeap) == 0 or len(self.maxHeap) == 0:
            return
        # the top of maxHeap shoudle be less then the top of minHeap
        # if not, then switch the top of the two heaps
        maxroot = -self.maxHeap[0]
        minroot = self.minHeap[0]
        if maxroot > minroot:
            # heapreplace: first heappop and then heappush
            heapq.heapreplace(self.maxHeap, -minroot)
            heapq.heapreplace(self.minHeap, maxroot)
            #print minroot, maxroot

'''Summary
算法武器：双堆（最大堆和最小堆）
'''