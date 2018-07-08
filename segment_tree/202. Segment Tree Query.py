'''
For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by the given root of segment tree.

Example
For array [1, 4, 2, 3], the corresponding Segment Tree is:

                  [0, 3, max=4]
                 /             \
          [0,1,max=4]        [2,3,max=3]
          /         \        /         \
   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
query(root, 1, 1), return 4

query(root, 1, 2), return 4

query(root, 2, 3), return 3

query(root, 0, 2), return 4
'''
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""

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
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if not root or start > end:
            return -sys.maxsize
            
        if start == root.start and end == root.end:
            return root.max
            
        mid = (root.start + root.end) // 2
        leftMax, rightMax = -sys.maxsize, -sys.maxsize
        # 判断对于给定的区间，我们是否需要在线段树的左侧查找
        # 注意我们的左侧区间是包括mid的，不要忘记=
        if start <= mid:
            # 左右两侧的区间的计算是有一个max和min的逻辑
            leftMax = self.query(root.left, max(root.start, start), min(end, mid))
        
        # 查看是否需要在右侧区间查找
        if end > mid:
            rightMax = self.query(root.right, max(mid + 1, start), min(root.end, end))

        # conquer阶段    
        return max(leftMax, rightMax)
            
'''
- 使用divide conquer, 递归方式求解一个给定区间的最大值
    - 因为我们的递归是有返回值的
- 最底层的递归返回计算：如果当前给定区间的start和end就是给定线段树的start和end，那么我就可以直接返回root.max
    - 最简单的情形就是线段树走到了叶子节点，其start和end的值相同，同时我们的区间也在每一层递归调用中被不断地缩小，最后start==end
- 当我们求解出给定区间的左侧最大和右侧最大的时候，我们conquer逻辑是再在其中取一个最大
- 注意我们在进行区间划分的时候有一个max和min的取值
'''