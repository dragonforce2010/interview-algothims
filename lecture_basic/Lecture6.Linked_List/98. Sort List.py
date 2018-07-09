'''
Sort a linked list in O(n log n) time using constant space complexity.

Example
Given 1->3->2->null, sort it to 1->2->3->null.

Challenge
Solve it by merge sort & quick sort separately.
'''
class Solution:
    def sortList(self, head):
        vals = []

        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        vals.sort()

        cur = head
        for val in vals:
            cur.val = val
            cur = cur.next

        return head
'''
算法武器：排序

算法思路：
定义一个数组，用于保存链表元素
扫描链表，将数据收集到定义的数组中
对数组中元素进行排序
扫描链表，按照数组中的值更新链表的节点值
'''
