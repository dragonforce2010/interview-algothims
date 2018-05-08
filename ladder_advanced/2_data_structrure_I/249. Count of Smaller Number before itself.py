'''Description
Give you an integer array (index from 0 to n-1, where n is the size of this array, data value from 0 to 10000) . For each element Ai in the array, count the number of element before this element Ai is smaller than it and return count number array.

 Notice
We suggest you finish problem Segment Tree Build, Segment Tree Query II and Count of Smaller Number first.
Example
For array [1,2,7,8,5], return [0,1,2,3,2]
'''
class SegmentTree:
    def __init__(self, start, end, count=0):
        self.start = start
        self.end = end
        self.count = count
        self.left, self.right = None, None
        
        
    @classmethod
    def build(cls, start, end, A):
        if start > end:
            return None
        
        if start == end:
            return SegmentTree(start, end)
        
        node = SegmentTree(start, end)
        mid = (start + end) / 2
        node.left = cls.build(start, mid, A)
        node.right = cls.build(mid + 1, end, A)
        node.count = node.left.count + node.right.count
        
        return node
    
    
    @classmethod
    def modify(cls, root, index, value):
        if not root:
            return
        
        if root.start == root.end:
            root.count = value
            return
        
        
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
            
        
        root.count = root.left.count + root.right.count
        
        
    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
        
        
        if start <= root.start and root.end <= end:
            return root.count
        
        
        return cls.query(root.left, start, end) + \
               cls.query(root.right, start, end)


class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    def countOfSmallerNumberII(self, A):
        if len(A) == 0:
            return []
            
        root = SegmentTree.build(0, max(A), A)
        
        results = []
        for a in A:
            results.append(SegmentTree.query(root, 0, a - 1))
            SegmentTree.modify(root, a, 1)
        
        return results
'''Summary
'''