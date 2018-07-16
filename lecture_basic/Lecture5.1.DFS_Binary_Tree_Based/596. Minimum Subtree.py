'''
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 
return the node 1.
'''
class Solution:
    def findSubtree(self, root):
        self.targetNode, self.minsum = None, sys.maxsize
        self.helper(root)
        return self.targetNode

    def helper(self, root):
        if not root:
            return 0

        # divide
        leftsum = self.helper(root.left)
        rightsum = self.helper(root.right)

        # conquer
        treesum = leftsum + rightsum + root.val
        if treesum < self.minsum:
            self.minsum = treesum
            self.targetNode = root

        return treesum
'''
算法武器：分治法（递归函数使用了返回值） + 遍历法(使用了全局变量，打擂台)

概念：

分治法的特点是使用了返回函数
遍历法的特点是使用了全局变量，用打擂台的形式进行计算
因为本题需要同时用到这两个特点，所以本题是分治法和遍历法的结合
算法思路：

使用分治法求给定树根的子树和。
分治函数的思路是首先计算左子树和，然后计算右子树和，最后加上根节点的值，三者之和构成了当前给定树根的子树和
同时在分治函数中使用打擂台的方式更新全局最小子树和以及子树根
'''