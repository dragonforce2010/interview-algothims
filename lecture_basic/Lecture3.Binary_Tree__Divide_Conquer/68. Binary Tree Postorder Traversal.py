'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [3,2,1].

Challenge
Can you do it without recursion?
'''
class Solution:
    def postorderTraversal(self, root):
        result = []
        self.posttraverse(root, result)
        return result

    def posttraverse(self, root, result):
        if not root:
            return 

        self.posttraverse(root.left, result)
        self.posttraverse(root.right, result)
        result.append(root.val)