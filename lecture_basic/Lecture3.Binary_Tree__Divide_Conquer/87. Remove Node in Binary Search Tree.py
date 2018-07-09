'''
Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

Example
Given binary search tree:

    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:

    5
   / \
  2   6
   \
    4
or

    5
   / \
  4   6
 /
2
'''
class Solution:
    def removeNode(self, root, value):
        self.ans = []
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)

    def inorder(self, root.left, value):
        if root is None:
            return

        self.inroder(root.left, value)
        # 中序遍历的时候过滤我们要删除的元素
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value

    # 以分治的方式，递归构建BST
    def build(self, l, r):
        if l == r:
            return TreeNode(self.ans[l])

        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(self.ans[mid])
        root.left = self.build(l, mid - 1)
        root.right = self.build(mid + 1, r)

        return root