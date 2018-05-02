'''Description
Find the kth smallest number in at row and column sorted matrix.
Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
'''
import heapq
# use heapq to resolve this problem
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # check the parameters if it's valid
        if not matrix or not k:
            raise Exception("Invalid parameter")
        # Two directions: down, right
        dirs = [
            (0,1), 
            (1,0)
        ]
        
        m, n = len(matrix), len(matrix[0])
        # initialize 
        visited = [[False] * n for _ in xrange(m)]
        heap = []
        # put (matrix[0][0], 0, 0) into heap
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        
        # pop k-1 times from heap
        for i in xrange(k - 1):
            _, x, y = heapq.heappop(heap)
            # loop through two directions: down, right
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                # check the boundary and visited array
                if nx < m and ny < n and not visited[nx][ny]:
                    # mark visited and push it to the heap
                    visited[nx][ny] = True
                    heapq.heappush(heap, (matrix[nx][ny], nx, ny))
        # pop the kth element from heap
        return heapq.heappop(heap)[0]
'''Summary
算法武器：堆 + 连续出队k-1次技巧
思路：

求第k大/小的问题都是要想到用堆这个武器来求解
然后用一个for循环连续出堆k - 1次
最后再进行一次出堆操作我们就得到了答案，我们在return部分直接返回这个答案
注意本题因为和坐标有关系，我们出堆一个最小元素之后，我们可以向右、向下将候选元素放入堆中（通过遍历方向数组计算获得新元素坐标），所以我们需要知道坐标信息，放入堆中的元素是一个三元组(元素值，元素x坐标，元素y坐标)
'''