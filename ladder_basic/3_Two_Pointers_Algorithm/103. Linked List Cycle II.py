'''
Given a linked list, return the node where the cycle begins.

If there is no cycle, return null.

Example
Given -21->10->4->5, tail connects to node index 1，return 10

Challenge
Follow up:

Can you solve it without using extra space?
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
    @param head: The first node of the linked list.
    @return: The node where the cycle begins. 
                if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if head == None or head.next == None:
            return None
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
            
        return None

'''
算法武器：快慢指针

算法思路：

进行参数检测
声明快慢指针
使用while循环，寻找环，并且找到slow和fast相遇的地方
如果slow和fast相等，那么使用一个while循环，让slow从链表首部开始走，让fast从当前位置走，走的速度都相同，直到他们相遇，即slow = fast，这个点就是环的起点
如果slow和fast不等，那么直接返回None
'''
