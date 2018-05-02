'''Description
Find K-th largest element in N arrays.
Example
In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.

In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is 7 and etc.
'''

import heapq
class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if not arrays or k < 1:
            raise Exception('Invalid parameter!')
            
        heap = []
        for arr in arrays:
            for ele in arr:
                heapq.heappush(heap, ele)
                if len(heap) > k:
                    heapq.heappop(heap)
                    
        return heap[0]

'''Summary
算法武器：堆

第k大元问题，还是一下子就要想到用堆，维护一个size为k的最小堆。因为本题数组没有排序，所以我们必须要用两个for循环将所有元素一次放入堆中。

放入元素的时候要注意：

对于每一个遍历到的元素直接放入
放置完元素之后检查尺寸，如果已经满尺寸k，则需要pop一个元素出去。因为我们建立的是小根堆，所以最小的元素会被淘汰。
当所有元素遍历完之后，堆中存放的元素就是最大的k个元素，我们要求的最大的k个元素就是堆顶元素
注意元素不断流入小根堆（尺寸为k）中，最终我们可以获得最大的k个元素。因为小根堆总是不断淘汰最小的元素

同理，如果元素不断流入尺寸为k的大根堆中，最终我们获得的是最小的k个元素，因为大根堆总是淘汰最大元素

所以以后根据题意，如果求第k大元，我们就建立维护k的小根堆
如果求第k小元，我们就建立维护k的大根堆

怎么建立大根堆？
- 只要将放入堆中的元素取反就行
'''