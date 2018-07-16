'''
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
return the node 11.
'''
class Solution:
    def findSubtree2(self, root):
        self.targetNode, self.average = None, 0
        self.helper(root)
        return self.targetNode

    # @return {(sum, average)}: the sum of the given tree, the average value of the given tree
    def helper(self, root):
        if root is None:
            return 0, 0

        # divide
        leftSum, leftSize = self.helper(root.left)
        rightSum, rightSize = self.helper(root.right)

        # conquer
        treesum = leftsum + rightsum + root.val
        size = leftSize + rightSize + 1
        average = treesum * 1.0 / size

        # 更新全局结果
        if self.targetNode is None or self.average < average:
            self.targetNode = root
            self.average = average

        # 返回本颗树的计算结果
        return treesum, size

# 算法武器： 分治法 + 递归 + 全局变量更新
