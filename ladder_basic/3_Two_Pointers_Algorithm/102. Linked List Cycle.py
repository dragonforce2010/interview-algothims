'''
Given a linked list, determine if it has a cycle in it.



Example
Given -21->10->4->5, tail connects to node index 1, return true

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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None or head.next is None:
            return False
        
        slow, fast = head, head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True    
'''
算法武器：链表 + 快慢指针

def hasCycle(self, head):
        # 当前节点为空或者当前节点是一个单节点，则返回无环
        if head is None or head.next is None:
            return False
        
        # 利用快慢指针，快指针指向第二个元素    
        slow, fast = head, head.next
        
        # 当快慢指针不相等时while循环继续
        while slow != fast:
            # 当快指针走到结尾为空则证明无环
            if fast is None or fast.next is None:
                return False
            
            # 慢指针走一步，快指针走两步    
            slow = slow.next
            fast = fast.next.next
        
        # 如果循环顺利跳出，则证明有环    
        return True 
'''