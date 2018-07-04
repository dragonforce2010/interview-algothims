'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
The following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Challenge
Your code should preferably run in O(n) time and use only O(1) memory.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA == 0 or lenB == 0:
            return None
        
        endA = self.getListEnd(headA)
        endA.next = headB
        hasCircle = False
        
        p, cnt = headA, 0
        while p:
            cnt += 1
            if cnt > lenA + lenB:
                hasCircle = True
                break
            p = p.next
            
        if not hasCircle:
            endA.next = None
            return None
        
        p1 = headA
        for x in range(lenB):
            p1 = p1.next
        
        p2 = headA
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        endA.next = None
        return p1

    def getListEnd(self, head):
        end = head
        while end.next:
            end = end.next
        return end

    def getListLen(self, head):
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        return size
        