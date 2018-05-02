'''Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

 Notice
Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.
Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge 
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    
    
    def flatten(self, root):
        if root is None:
            return
            
        self.helper(root)
        
    
    # flatten the give tree and return the last tree node
    # @return {lastTreeNode} the last tree node
    def helper(self, root):
        if root is None:
            return None
            
        # divide
        lastLeftNode = self.helper(root.left)
        lastRightNode = self.helper(root.right)
        
        # conquer
        # only when lastLeftNode exists, we need to do the conquer
        if lastLeftNode:
            lastLeftNode.right = root.right
            root.right = root.left
            root.left = None
        
        # caculate lastNode and return it
        if lastRightNode:
            return lastRightNode
            
        if lastLeftNode:
            return lastLeftNode
            
        return root
'''Summary
算法武器：分治法
注意释放左指针, 即 root.left = None
'''
