'''
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree and contain at least one node in it.

Example
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
'''
class Solution:
    def maxPathSum2(self, root):
        if root is None:
            return 0

        # divide
        leftSum = self.maxPathSum2(root.left)
        rightSum = self.maxPathSum2(root.right)

        # conquer
        return max(leftSum, rightSum, 0) + root.val
