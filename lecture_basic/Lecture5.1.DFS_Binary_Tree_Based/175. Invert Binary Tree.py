'''
Invert a binary tree.

Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
Challenge
Do it in recursion is acceptable, can you do it without recursion?
'''
class Solution:
    def invertBinaryTree(self, root):
        if node is None:
            return node

        # divide
        invertedLeft = self.invertBinaryTree(self.left)
        invertedRight = self.invertBinaryTree(self.right)

        # conquer
        node.left, node.right = invertedRight, invertedLeft

        return node