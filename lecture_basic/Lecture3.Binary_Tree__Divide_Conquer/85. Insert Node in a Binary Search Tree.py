'''
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

Example
Given binary search tree as follow, after Insert node 6, the tree should be:

  2             2
 / \           / \
1   4   -->   1   4
   /             / \ 
  3             3   6
Challenge
Can you do it without recursion?
'''
class Solution:
    def insertNode(self, root, node):
        if root is None:
            return node

        curt = root

        # while 的结束条件是curt == node，也就是我们把node正确插入到树中后这个条件会成立
        while curt != node:
            if node.val < curt.val:
                # 每当我们向左走的时候，我们需要检查是否左侧节点为空，如果为空，那么cur.left就是我们的插入位置
                if curt.left is None:
                    curt.left = node
                # 不论cur.left是空与否，我们都需要向左走一步
                # 如果curt的left是空，并且我们插入了元素，那么我们向左走一步之后就会使得curt == node，这样循环就可以结束了
                curt = curt.left
            # 如果要插入的元素就在树中，那么我们直接返回
            elif node.val == curt.val:
                return curt
            else:
                if curt.right is None:
                    curt.right = node
                curt = curt.right

        return root
