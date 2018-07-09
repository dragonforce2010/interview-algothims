'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
'''
from collections import deque
class Solution:
    def levelOrderButtom(self, root):
        if root is None:
            return []

        result, queue = [], deque([root])

        while queue:
            size = len(queue)
            levelRes = []
            for i in range(size):
                node = queue.popleft()
                levelRes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(levelRes)

        return list(reversed(result))
