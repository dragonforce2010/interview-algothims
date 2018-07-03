'''
Merge k sorted linked lists and return it as one sorted list.

Analyze and describe its complexity.

Example
Given lists:

[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
'''
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        
        import heapq
        # 因为我们想要按照node.val的值进行排序，所以这里我们把node.val放在元组的第一个位置
        heap = [ (node.val, node) for node in lists if node]
        # 构建堆的过程中要尤为注意堆化的操作，如果我们初始化数组时，数组中额数据不止一个，那么我们就要使用
        # heapq的heapify()函数将当前堆进行堆化
        heapq.heapify(heap)
        
        dummyhead = cur = ListNode(0)
        while heap:
            val, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
                
        return dummyhead.next
        