'''Descritpion
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge 
O(n) time complexity
'''
class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        for pos in range((len(A) - 1) / 2, -1, -1):
            self.siftdown(A, pos)
            
    def siftdown(self, A, rootPos):
        while rootPos * 2 + 1 < len(A):
            son = rootPos * 2 + 1
            if son + 1 < len(A) and A[son + 1] < A[son]:
                son = son + 1
            if A[rootPos] <= A[son]:
                break
            
            A[rootPos], A[son] = A[son], A[rootPos]
            rootPos = son
'''Summary
算法武器：建堆

本题考查建堆（二叉堆）的实现。建堆的过程如下：
- 从二叉树的最后一个拥有孩子的父节点开始，逐步向上（到树根节点）进行下滑操作，将每个节点为根的子树调整成一个堆，直到整个树成为一个堆。
- 下滑操作的过程：从给定的树根节点开始，将树根节点和两个孩子比较，取两个孩子中最小的节点和树根节点比较，如果比根小，那么根节点和该子节点交换，然后递归向下调整，知道该子树成为一个堆。
'''