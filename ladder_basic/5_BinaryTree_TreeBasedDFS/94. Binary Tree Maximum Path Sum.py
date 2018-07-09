'''
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Example
Given the below binary tree:

  1
 / \
2   3
return 6.
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        if root is None:
            return -sys.maxsize
            
        maxPathSum, _ = self.maxPathSumHelper(root)
        
        return maxPathSum
        
    def maxPathSumHelper(self, root):
        # root 为空时，root2AnyPathSum我们初始化为0，表示不选择任何点到root2AnyPath中
        # maxPathSum我们必须初始化为最小值，因为它要参与上层计算
        if root is None:
            return (-sys.maxsize, 0)

        # divide    
        leftMaxPathSum, leftRoot2AnyPathSum = self.maxPathSumHelper(root.left)
        rightMaxPathSum, rightRoot2AnyPathSum = self.maxPathSumHelper(root.right)
        
        # conquer分为连个部分
        # - 计算root2AnyPathSum
        # - 计算maxPathSum
        root2AnyPathSum = max(leftRoot2AnyPathSum, rightRoot2AnyPathSum, 0) + root.val
        # maxPathSum的conquer包括三种情况
        # - 结果在左子树
        # - 结果在右子树
        # - 结果可能经过根节点，我们需要通过root2AnyPathSum计算得到
        maxPathSum = max(leftMaxPathSum,\
                         rightMaxPathSum,\
                         max(leftRoot2AnyPathSum, 0) + max(rightRoot2AnyPathSum, 0) + root.val)
        
        return maxPathSum, root2AnyPathSum
'''
- 这道题的思路是分治法
- 了解两个概念
    - maxPathSum：任意节点到任意节点的路径Sum， 这个路径至少包括一个节点，因为我们的答案要依赖这个计算
    - root2AnyPathSum: 从根节点到任意节点的路径sum， 这个路径可以是空，因为我们的答案可能包括这个部分，或者不包括这个部分

'''