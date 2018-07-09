'''
Given a list, rotate the list to the right by k places, where k is non-negative.

Example
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
'''
class Solution:
    '''
    1.求整个链表长度
    2.对k进行取模，得到有效的k值（k可能比整个链表长度长）
    3.扫描链表直到size - k,找到新的链表头nhead的前驱
        - 将前驱的next置为空
    4.从nhead扫描，直到链表结尾，让结尾节点指向元链表head，构成一条新链
    '''
    def rotateRight(self, head, k):
        if not head or not head.next or not k:
            return head

        size, curNode = 0, head
        while curNode:
            size += 1
            curNode = curNode.next

        k = k % size
        # 如果k是链表长度的整个倍数，那么就相当于没有rotate
        if k == 0:
            return head

        # 因为我们的curNode指向的是head，所以我们把当前的curLength初始化为1
        curLength, curNode = 1, head
        while curLength < size - k:
            curNode = curNode.next
            curLength += 1

        # curNode跳出循环后刚好指向新链表头的前驱
        nhead = curNode.next
        curNode.next = None
        curNode = nhead

        while curNode.next:
            curNode = curNode.next

        curNode.next = head

        return nhead
