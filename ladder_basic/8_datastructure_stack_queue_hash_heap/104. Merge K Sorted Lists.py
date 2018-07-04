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
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
                
        import heapq        
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        return head.next

'''
算法武器： heap + list + dummy head

我们使用堆的方式和使用队列的模式有相同模式，即我们使用一个while循环，一次从堆中取出元素，进行操作，同时随着操作右不断地向堆中加入元素，知道堆中的元素被处理完毕。

思路和求解过程：

合并多个链表的问题一定是使用堆
扫描链表的链表，把每个链表的头结点加入到堆中
放入堆中的元素是一个二元组，第一个元素是node.val，堆会根据这个值进行排序
使用虚拟头结点简化计算
每当出堆一次，就查看出堆的链表节点是否还有下一个节点，如果有，就将其入堆
'''