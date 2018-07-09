'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''
class DoublyListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = self.prev = next

class Solution:
    def bstToDoublyList(self, root):
        inorder = []
        self.inorderTraverse(root, inorder)
        if not inorder:
            return None

        dummyHead = DoublyListNode(0)
        prev = dummyHead

        # 形成一个链表，我们选择尾插法
        # 插入一个元素，我们需要借助前驱节点
        for val in inorder:
            node = DoublyListNode(val)
            prev.next = node
            node.prev = prev
            prev = node

        return dummyHead.next

    def inorderTraverse(self, root, inorder):
        if root is None:
            return

        self.inorderTraverse(root.left, inorder)
        inorder.append(root.val)
        self.inorderTraverse(root.right, inorder)

'''
算法武器：二叉树中序遍历 + 双向链表构成
双向链表的构建需要使用到prev节点，同时使用dummy节点使头的处理简单
'''