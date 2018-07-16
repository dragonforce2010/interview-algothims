'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Example
An example:

  2
 / \
1   4
   / \
  3   5
The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).
'''
'''
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''

class Solution:
    def isValidBST(self, root):
        if root is None:
            return True

        isBST, minValue, maxValue = self.helper(root)
        return isBST

    # validate if the tree root is bst, calcuate the max/min value of the tree
    # @return {isBST, minValue, maxValue}
    def helper(self, root):
        if root is None:
            return True, sys.maxsize, -sys.maxsize

        # divide
        isLeftBST, leftMinVal, leftMaxVal = self.helper(root.left)
        isRightBST, rightMinVal, rightMaxVal = self.helper(root.right)

        # conquer
        isBST = True
        minVal = min(leftMinVal, root.val)
        maxVal = max(rightMaxVal, root.val)

        if not isLeftBST or not isRightBST:
            isBST = False

        if root.left and leftMaxVal >= root.val or root.right and rightMinVal <= root.val:
            isBST = False

        return isBST, minVal, maxVal