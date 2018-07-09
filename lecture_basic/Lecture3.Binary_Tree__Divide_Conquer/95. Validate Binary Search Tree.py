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
class Solution:
    def isValidBST(self, root):
        if root is None:
            return True

        isBST, minValue, maxValue = self.helper(root)
        return isBST

    def helper(self, root):
        # 这里的初始化要注意：我们必须初始化为最大最小极值情形
        if root is None:
            return True, sys.maxsize, -sys.maxsize

        isLeftBST, leftMinValue, leftMaxValue = self.helper(root.left)
        isRightBST, rightMinValue, rightMaxValue = self.helper(root.right)

        # 对min,max value的计算使用min，max函数进行的，这个部分可以和初始化部分相对
        # 因为初始化部分的初始设置合理，所以当我们处理叶子节点的时候，可以获得正确答案
        minValue = min(leftMinValue, root.val)
        maxValue = max(rightMaxValue, root.val)

        if not isLeftBST or not isRightBST:
            return False, minValue, maxValue

        # 从反方向证明非BST的情况
        if root.left and leftMaxValue >= root.val or root.right and rightMinValue <= root.val:
            return False, minValue, maxValue

        return True, minValue, maxValue   