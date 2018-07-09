'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3
 

return [1,3,2].
'''
class Solution:
    # 非递归解法
    def inorderTraversal1(self, root):
        if root is None:
            return []

        '''
        - curr：指向当前需要处理的树根/子树根
        - stack：用于保存一路扫描过的根节点当我们寻找curr所指的树的最左节点的时候
        - while循环的条件就是只要curr当前待处理的树不为空，或是栈里保存的树根不为空
        '''
        stack, result, curr = [], [], root
        while curr or stack:
            # 如果当前需要处理的子树不为空，我们就需要一直不断地走到该树的最左节点
            # 如果没有需要处理的子树，那么我们就从栈里pop出树根进行处理
            while curr:
                stack.append(curr)
                curr = curr.left
                
            node = stack.pop()
            result.append(node.val)
            # 因为是根左右的方式进行遍历，上面对node节点的访问相当于访问了根和左子，接下来是访问右子，所以我们向右走一步
            # 如果右子树不为空的话，我们的while循环中就需要一直不断地走到该子树的最左侧，重复上面的步骤
            curr = node.right

        return result

    # 使用分治法求解
    def inorderTraversal2(self, root):
        if root is None:
            return []

        # divide
        leftRes = self.inorderTraversal2(root.left)
        rightRes = self.inorderTraversal2(root.right)

        # conquer
        result = []
        result.extend(leftRes)
        result.append(node.val)
        result.extend(rightRes)

        return result