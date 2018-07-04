'''
Find the middle node of a linked list.

Example
Given 1->2->3, return the node with value 2.

Given 1->2, return the node with value 1.

Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?
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
    @param: head: the head of linked list.
    @return: a middle node of the linked list
    """
    
    # 使用快盘指针寻找链表中点
    def middleNode(self, head):
        # write your code here
        if not head:
            return None
            
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow