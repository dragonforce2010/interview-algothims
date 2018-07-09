'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example
Given:

    1
   / \
  2   3
 / \
4   5
return [1,2,4,5,3].
'''
class Solution:
    def preorderTraversal(self, root):
        if root is None:
        return []

    stack = []
    preorder = []

    while stack:
        node = stack.pop()
        preorder.append(node.val)
        # 因为stack中的顺序是反的，所以我们如果想以根左右的方式访问，我们就必须先把右子树入栈，然后左子树入栈
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return preorder
        