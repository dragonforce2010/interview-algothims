'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Challenge
Challenge 1: Using only 1 queue to implement it.

Challenge 2: Use DFS algorithm to do it.
'''
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result, queue = [], deque([root])

        while queue:
            # 因为需要记录每一层结果，所以首先求出当前层的size，然后在遍历当前层元素
            size = len(queue)
            layerRes = []
            for i in range(size):
                node = queue.popleft()
                layerRes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layerRes)

        return [map(lambda node: node.val, l) for l in result]