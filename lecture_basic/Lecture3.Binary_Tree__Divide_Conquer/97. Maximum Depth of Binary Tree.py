'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example
Given a binary tree as follow:

  1
 / \ 
2   3
   / \
  4   5  
The maximum depth is 3.
'''
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0

        # divide
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        # conquer
        return max(leftDepth, rightDepth) + 1