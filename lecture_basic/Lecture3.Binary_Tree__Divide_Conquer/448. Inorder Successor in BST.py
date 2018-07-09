'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.

Example
Given tree = [2,1] and node = 1:

  2
 /
1
return node 2.

Given tree = [2,1,3] and node = 2:

  2
 / \
1   3
return node 3.

Challenge
O(h), where h is the height of the BST.
'''
class Solution:
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None

        curt, successor = root, None

        # 注意：我们在查找p元素的同时，我们记录successor（当我们向左走的时候）
        while curt and curt.val != p.val:
            if curt.val > p.val:
                successor = curt
                curt = curt.left
            else:
                curt = curt.right

        if curt is None:
            return None

        # 如果右子树不存在，那么前驱节点一定是successor所指节点
        if curt.right is None:
            return successor

        # 如果右子树存在，我们需要走到右子树的最左
        curt = curt.right
        while curt.left:
            curt = curt.left

        return curt