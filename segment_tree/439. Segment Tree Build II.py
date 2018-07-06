'''
The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment / interval.

start and end are both integers, they should be assigned in following rules:

The root's start and end is given by build method.
The left child of node A has start=A.left, end=(A.left + A.right) / 2.
The right child of node A has start=(A.left + A.right) / 2 + 1, end=A.right.
if start equals to end, there will be no children for this node.
Implement a build method with a given array, so that we can create a corresponding segment tree with every node value represent the corresponding interval max value in the array, return the root of this segment tree.

Example
Given [3,2,1,4]. The segment tree will be:

                 [0,  3] (max = 4)
                  /            \
        [0,  1] (max = 3)     [2, 3]  (max = 4)
        /        \               /             \
[0, 0](max = 3)  [1, 1](max = 2)[2, 2](max = 1) [3, 3] (max = 4)
'''
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        return self.buildTree(A, 0, len(A) - 1)
        
    def buildTree(self, A, start, end):
        if start > end:
            return None
        
        # 根据区间构造树根节点，这里把max初始化为A[start],这个值会后来被子树自底向上更新
        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root

        # 划分子区间，递归调用构建线段树    
        mid = (start + end) // 2    
        root.left = self.buildTree(A, start, mid)
        root.right = self.buildTree(A, mid + 1, end)
        
        # 以下部分是自底向上更新线段树的每个节点的max值
        if root.left:
            root.max = max(root.max, root.left.max)
            
        if root.right:
            root.max = max(root.max, root.right.max)
            
        return root