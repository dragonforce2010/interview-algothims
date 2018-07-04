'''
Find the kth smallest numbers in an unsorted integer array.

Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
'''
class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    # def kthSmallest(self, k, nums):
    #     # Write your code here
    #     import heapq
    #     heapq.heapify(nums)
    #     return heapq.nsmallest(k, nums)[-1]
        
    def kthSmallest(self, k, nums):
        import heapq
        heap = []
        for elem in nums:
            heapq.heappush(heap, -elem)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return -heap[0]

'''
算法武器：大根堆(将元素取负值入堆构建大根堆) + 固定尺寸
答案：返回堆顶元素（别忘记加负号）

第k小元问题，还是一下子就要想到用堆，维护一个size为k的最小堆。
放入元素的时候要注意：
对于每一个遍历到的元素直接放入
放置完元素之后检查尺寸，如果已经满尺寸k，则需要pop一个元素出去。因为我们建立的是大根堆，所以最大的元素会被淘汰。
当所有元素遍历完之后，堆中存放的元素就是最小的k个元素，我们要求的最小的第k个元素就是堆顶元素
注意元素不断流入大根堆（尺寸为k）中，最终我们可以获得最小的k个元素。因为大根堆总是不断淘汰最大的元素
同理，如果元素不断流入尺寸为k的小根堆中，最终我们获得的是最大的k个元素，因为小根堆总是淘汰最小元素
所以以后根据题意，如果求第k大元，我们就建立维护k的小根堆
如果求第k小元，我们就建立维护k的大根堆
怎么建立大根堆？

只要将放入堆中的元素取反就行

'''