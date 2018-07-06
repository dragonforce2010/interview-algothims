'''
For a Maximum Segment Tree, which each node has an extra value max to store the maximum value in this node's interval.

Implement a modify function with three parameter root, index and value to change the node's value with [start, end] = [index, index] to the new given value. Make sure after this change, every node in segment tree still has the max attribute with the correct value.

Example
For segment tree:

                      [1, 4, max=3]
                    /                \
        [1, 2, max=2]                [3, 4, max=3]
       /              \             /             \
[1, 1, max=2], [2, 2, max=1], [3, 3, max=0], [4, 4, max=3]
if call modify(root, 2, 4), we can get:

                      [1, 4, max=4]
                    /                \
        [1, 2, max=4]                [3, 4, max=3]
       /              \             /             \
[1, 1, max=2], [2, 2, max=4], [3, 3, max=0], [4, 4, max=3]
or call modify(root, 4, 0), we can get:

                      [1, 4, max=2]
                    /                \
        [1, 2, max=2]                [3, 4, max=0]
       /              \             /             \
[1, 1, max=2], [2, 2, max=1], [3, 3, max=0], [4, 4, max=0]
Challenge
Do it in O(h) time, h is the height of the segment tree.
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
    @param root: The root of segment tree.
    @param index: index.
    @param value: value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if not root:
            return
        
        # 线段树的更新一定发生在叶子节点，所以我们要查看给定的index是否就是线段树root的叶子区间
        # 线段树的叶子区间特点是start = end
        if root.start == index and root.end == index:
            root.max = value
            return
        
        # 计算mid值，然后划分区间，进而递归更新
        mid = (root.start + root.end) // 2

        # 判断要更新的区间是否在线段树的左子区间
        if 0 <= index <= mid:
            self.modify(root.left, index, value)

        # 判断要更新的区间是否在线段树的右子区间    
        if mid + 1 <= index <= root.end:
            self.modify(root.right, index, value)
            
        # 当线段树叶子节点区间被更新后需要自底向上更新线段树的当前区间最大值
        root.max = max(root.left.max, root.right.max)
