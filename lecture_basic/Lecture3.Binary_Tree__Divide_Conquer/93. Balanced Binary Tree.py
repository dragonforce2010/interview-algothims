'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3 
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.
'''
class Solution:
    '''
    @param root: The root of binary tree
    @return: True if this binary tree is balanced, or false
    '''
    def isBalanced(self, root):
        isBalanced, height = self.helper(root)
        return isBalanced

    def helper(self, root):
        if root is None:
            return True, 0

        # divide 
        leftIsBalanced, leftHeight = self.helper(root.left)
        rightIsBalanced, rightHeight = self.helper(root.right)

        # conquer
        if leftIsBalanced and rightIsBalanced and abs(leftHeight - rightHeight) <= 1:
            return True, max(leftHeight, rightHeight) + 1

        return False, max(leftHeight, rightHeight) + 1