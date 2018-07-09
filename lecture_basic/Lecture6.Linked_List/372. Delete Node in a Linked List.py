'''
Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

Example
Linked list is 1->2->3->4, and given node 3, delete the node in place 1->2->4
'''
class Solution:
    def deleteNode(self, node):
        if node is None or node.next is None:
            return 

        next = node.next
        node.val = next.val
        node.next = next.next

        return

'''
本题的难点在于我们只给定了要删除的节点，并且该链表是单向链表
解决方案: 我们改变当前需要删除节点的val和next，达到删除当前节点的目的
'''