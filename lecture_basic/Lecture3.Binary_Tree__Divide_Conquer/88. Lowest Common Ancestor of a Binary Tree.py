'''
Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

Example
For the following binary tree:

  4
 / \
3   7
   / \
  5   6
LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7
'''
class Solutioin:
    # 注意本题已经规定给定的节点A和B一定是在树中
    def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None

        if root == A or root == B:
            return root

        leftLCA = self.lowestCommonAncestor(root.left, A, B)
        rightLCA = self.lowestCommonAncestor(root.right, A, B)

        if leftLCA and rightLCA:
            return root

        if leftLCA is None:
            return rightLCA

        if rightLCA is None:
            return leftLCA