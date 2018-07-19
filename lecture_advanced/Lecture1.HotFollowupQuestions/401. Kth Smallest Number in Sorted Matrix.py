'''
Find the kth smallest number in at row and column sorted matrix.

Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5

Challenge
Solve it in O(k log n) time where n is the bigger one between row size and column size.
'''
import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        if not matrix or k < 1:
            raise Exception("Invalid parameter")

        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        dirs = [
            (0, 1),
            (1, 0)
        ]
        visited = set()

        for i in range(k - 1):
            if not heap:
                raise Exception("K is not a valid parameter, it should be larger than the number of matrix cells")

            _, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and (nx, ny) not in visited:
                    heapq.heappush(heap, (matrix[nx][ny], nx, ny))
                    visited.add((nx, ny))

        return heapq.heappop(heap)[0]

'''
算法武器：堆 + 连续出队k-1次技巧
思路：

求第k大/小的问题都是要想到用堆这个武器来求解
然后用一个for循环连续出堆k - 1次
最后再进行一次出堆操作我们就得到了答案，我们在return部分直接返回这个答案
注意本题因为和坐标有关系，我们出堆一个最小元素之后，我们可以向右、向下将候选元素放入堆中（通过遍历方向数组计算获得新元素坐标），所以我们需要知道坐标信息，放入堆中的元素是一个三元组(元素值，元素x坐标，元素y坐标)
'''
        

