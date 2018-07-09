'''
Reverse a linked list from position m to n.

Example
Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.

Challenge
Reverse it in-place and in one-pass
'''
class Solution:
    def reverseBetween(self, head, m, n):
        if head is None or m >= n or head.next is None:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head

        preMthNode = self.findKth(dummyHead, m - 1)
        mthNode = preMthNode.next
        nthNode = self.findNth(dummyHead, n)
        postNthNode = nthNode.next
        nthNode.next = None

        self.reverse(mthNode)

        mthNode.next = postNthNode
        preMthNode.next = nthNode

        return dummyHead.next

    def findKth(self, head, k):
        if not head or k < 0:
            return None
        
        cur = head
        for i in range(k):
            if cur:
                cur = cur.next
            else:
                return None

        return cur

    def reverse(self, head):
        if head is None:
            return None

        prev, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

'''
解题关键是画图，了解在整个翻转过程中，preMthNode, mthNode, nthNode, postNthNode的重要性

学会对一个链表进行翻转：
定义三个指针进行翻转操作（prev, curr, next）
使用一个while循环进行列表翻转
while的循环条件为curr不为空
while退出后，prev指向翻转后的列表的头结点
翻转4部曲

保存next指针
当前指针后继指向前驱
前驱向后移动，指向当前
当前向后移动，指向next
'''