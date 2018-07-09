'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example
Given 1->4->3->2->5->2->null and x = 3,
return 1->2->2->4->3->5->null.
'''
class Solution:
    def partition(self, head, x):
        if head is None:
            return head

        aHead, bHead = ListNode(0), ListNode(0)
        aTail, bTail = aHead, bHead

        cur = head
        while cur:
            if cur.val < x:
                aTail.next = cur
                aTail = aTail.next
            else:
                bTail.next = cur
                bTail = bTail.next
            cur = cur.next

        bTail.next = None
        aTail.next = bHead.next

        return aHead.next

'''
算法武器：链表 + dummyNode + 双链表头指针 + 双链表尾指针 + 双链表连接

算法思路：

定义两个链表的dummy头结点aHead, bHead
定义两个聊表的尾指针aTail, bTail, 其初值为头结点
定义当前游标指针，用于遍历整个给定链表
aTail和bTail是游标指针，aTail指向node节点值小于x的链表
bTail指向node节点值大于等于x的链表
使用while循环遍历整个链表，对于扫描到的每一个节点元素
如果cur.val < x, 则把它加入到aHead的链表中，即让aTail.next = cur, 然后移动aTail， aTail = aTail.next
如果cur.val >=x, 则把它加入到bHead的链表中，即让bTail.next = cur, 然后移动bTail， bTail = bTail.next
移动游标指针，让其指向下一个元素
让aHead链表和bHead链表进行拼接， aTail.next = bHead.next
不要忘记将aTail.next置空， aTail.next = 0
返回aHead.next
'''
