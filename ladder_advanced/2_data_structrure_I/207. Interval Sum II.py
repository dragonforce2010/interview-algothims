'''Description
Given an integer array in the construct method, implement two methods query(start, end) and modify(index, value):

For query(start, end), return the sum from index start to index end in the given array.
For modify(index, value), modify the number in the given index to value
 Notice
We suggest you finish problem Segment Tree Build, Segment Tree Query and Segment Tree Modify first.
Example
Given array A = [1,2,7,8,5].

query(0, 2), return 10.
modify(0, 4), change A[0] from 1 to 4.
query(0, 1), return 6.
modify(2, 1), change A[2] from 7 to 1.
query(2, 4), return 14.
Challenge 
O(logN) time for query and modify.
'''
class SegmentTree(object):
    
    def __init__(self, start, end, sum=0):
        self.start = start
        self.end = end
        self.sum = sum
        self.left, self.right = None, None 

    @classmethod
    def build(cls, start, end, a):
        if start > end:
            return None
		
        # if it's leaf segment
        if start == end:
            return SegmentTree(start, end, a[start])

        # if it's not leaf segment, we split the segment
        node = SegmentTree(start, end, a[start])
        mid = (start + end) / 2
        node.left = cls.build(start, mid, a)
        node.right = cls.build(mid + 1, end, a)
        # update the value of this segment based on its children
        node.sum = node.left.sum + node.right.sum
        
        return node
        

    @classmethod
    def modify(cls, root, index, value):
        if root is None:
            return

        # if it's leaf segment, update the value
        if root.start == root.end:
            root.sum = value
            return
    
        # if it's not leaf segment, based on index position, we recursively go to child's segment    
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        
        # update the current non-leaf segment value
        root.sum = root.left.sum + root.right.sum

    @classmethod
    def query(cls, root, start, end):
        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:
            return root.sum
        
        return cls.query(root.left, start, end) +  \
               cls.query(root.right, start, end)


class Solution:	
    # @param A: An integer list
    def __init__(self, A):
        # write your code here
        self.root = SegmentTree.build(0, len(A)-1, A)
    

    # @param start, end: Indices
    # @return: The sum from start to end
    def query(self, start, end):
        # write your code here
        return SegmentTree.query(self.root, start, end)
    

    # @param index, value: modify A[index] to value.
    def modify(self, index, value):
        # write your code here
        SegmentTree.modify(self.root, index, value)
'''Summary
'''