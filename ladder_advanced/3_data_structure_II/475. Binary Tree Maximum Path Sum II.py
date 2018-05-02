'''Description
Given a binary tree, find the maximum path sum from root.

The path may end at any node in the tree and contain at least one node in it.
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    #solution1
    
    def maxPathSum2(self, root):
        if root is None:
            return 0
        
        sum_left = self.maxPathSum2(root.left)
        sum_right = self.maxPathSum2(root.right)
        
        #conquer
        return max(sum_left, sum_right, 0) + root.val
        
'''Summary
算法武器：分治

本题求解的是从树根到任意节点的单条路径的最大path sum。
所以使用分治的策略是：
- 求左子树单路径最大sum
- 求右子树单路径最大sum
- 选择左右子树path sum最大的，同时还要和0比较，因为可能有负值存在， 然后加上根节点

二叉树问题，首先想分治的解决思路，将问题在子树中解决，然后合并答案。

# 返回root树的最大从根到叶子节点的路径sum
    # 该定义满足递归定义，所以直接在解决方案中递归调用此函数
    def maxPathSum2(self, root):
        # 递归结束条件：走到叶子节点
        # 叶子节点的maxPathSum为0
        if root is None:
            return 0

        #divide 分治求左右子树中的root -》leaf的最大pathSum
        sum_left = self.maxPathSum2(root.left)
        sum_right = self.maxPathSum2(root.right)

        #conquer
        # 选择左右子树中的最大的一个pathSum和根节点相连
        return max(sum_left, sum_right, 0) + root.val
'''