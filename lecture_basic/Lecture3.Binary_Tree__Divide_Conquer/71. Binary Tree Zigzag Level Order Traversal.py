'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

Example
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7
 

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]
'''
from collections import deque
def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result, queue, currentLevel = [], deque([root]), 1

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

            if currentLevel % 2 == 0:
                levelRes.reverse()  
                  
            result.append(levelRes)
            currentLevel += 1

        return result