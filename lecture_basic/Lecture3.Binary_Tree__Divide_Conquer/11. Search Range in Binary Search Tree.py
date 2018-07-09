'''
Given a binary search tree and a range [k1, k2], return all elements in the given range.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
'''
class Solution:
    def searchRange1(self, root, k1, k2):
        if root is None:
            return []

        ans, queue, index = [], [root], 0

        while index < len(queue):
            node = queue[index]
            if k1 <= node.val <= k2:
                ans.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            index += 1

        return sorted(ans)

    def searchRange2(self, root, k1, k2):
        if root is None:
            return []

        from collections import deque
        ans, queue = [], deque([root])

        while queue:
            node = queue.popleft()
            if k1 <= node.val <= k2:
                ans.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            
        return sorted(ans)

    def searchRange3(self, root, k1, k2):
        if k1 > k2:
            return []

        result = []

        for target in range(k1, k2 + 1):
            if self.searchTarget(root, target):
                result.append(target)

            return result

    def searchTarget(self, root, target):
        if root is None:
            return False

        if root.val == target:
            return True
        elif root.val < target:
            return self.searchTarget(root.right, target)
        else:
            return self.searchTarget(root.left, target)