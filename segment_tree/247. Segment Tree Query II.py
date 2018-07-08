'''
For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of elements in the the array which value is between interval start and end. (The array may not fully filled by elements)

Design a query method with three parameters root, start and end, find the number of elements in the in array's interval [start, end] by the given root of value SegmentTree.

Example
For array [0, 2, 3], the corresponding value Segment Tree is:

                     [0, 3, count=3]
                     /             \
          [0,1,count=1]             [2,3,count=2]
          /         \               /            \
   [0,0,count=1] [1,1,count=0] [2,2,count=1], [3,3,count=1]
query(1, 1), return 0

query(1, 2), return 1

query(2, 3), return 2

query(0, 2), return 2
'''
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if not root or start > end:
            return 0
            
        if root.start == start and root.end == end:
            return root.count
            
        mid = (root.start + root.end) // 2
        leftCount, rightCount = 0, 0
        
        if start <= mid:
            leftCount = self.query(root.left, max(root.start, start), min(end, mid))
            
        if end > mid:
            rightCount = self.query(root.right, max(mid + 1, start), min(end, root.end))
            
        return leftCount + rightCount
'''
- 使用divide conquer, 递归方式求解一个给定区间的count
    - 因为我们的递归是有返回值的
- 最底层的递归返回计算：如果当前给定区间的start和end就是给定线段树的start和end，那么我就可以直接返回root.count
    - 最简单的情形就是线段树走到了叶子节点，其start和end的值相同，同时我们的区间也在每一层递归调用中被不断地缩小，最后start==end
- 当我们求解出给定区间的左侧count和右侧count的时候，我们conquer逻辑是将两个count相加
- 注意我们在进行区间划分的时候有一个max和min的取值
'''