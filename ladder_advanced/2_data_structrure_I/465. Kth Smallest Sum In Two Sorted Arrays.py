'''Description
Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.
Example
Given [1, 7, 11] and [2, 4, 6].

For k = 3, return 7.

For k = 4, return 9.

For k = 8, return 15.

Challenge 
Do it in either of the following time complexity:

O(k log min(n, m, k)). where n is the size of A, and m is the size of B.
O( (m + n) log maxValue). where maxValue is the max number in A and B.
'''
import heapq
# Use two pointers
class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    # Solution 1
    def kthSmallestSum1(self, A, B, k):
        if not A or not B or not k:
            raise Exception("Invalid parameter")
        # Two directions: down, right
        dx, dy = (0,1), (1,0)
        m, n = len(A), len(B)
        # initialize 
        visited = set()
        heap = []
        # put (matrix[0][0], 0, 0) into heap
        heapq.heappush(heap, ((A[0] + B[0], 0, 0)))
        visited.add((0,0))
        
        # pop k-1 times from heap
        for i in xrange(k - 1):
            # x: the pointer pos in A
            # y: the pointer pos in B
            _, x, y = heapq.heappop(heap)
            # loop through two directions: down, right
            for j in xrange(2):
                nx = x + dx[j]
                ny = y + dy[j]
                # check the boundary and visited array
                if nx < m and ny < n and (nx, ny) not in visited:
                    # mark visited and push it to the heap
                    visited.add((nx, ny))
                    heapq.heappush(heap, (A[nx] + B[ny], nx, ny))
        # pop the kth element from heap
        return heapq.heappop(heap)[0]
    
    def kthSmallestSum(self, A, B, k):
        if not A or not B:
            return 0
        import heapq
        heap = []
        m, n = len(A), len(B)
        for i in range(min(k, n)):
            heapq.heappush(heap, (A[0] + B[i], 0, i))
        
        while k > 1:
            _, x, y = heapq.heappop(heap)
            if x + 1 < m:
                heapq.heappush(heap, (A[x + 1] + B[y], x + 1, y))
            k -= 1
        return heapq.heappop(heap)[0]
'''Summary
算法武器：堆

注意本题中使用了一个访问数组，这个数组空间通常得开和给定输入一样大的规模，但是本题使用了set，不需要提前开辟空间，动态添加已经处理过的元素，这样可以避免内存问题。

这是第k小元问题，一定要想到堆这个武器。一般思路是：

构建一个size为k的最小堆
用while循环连续进行出堆操作k - 1次
返回答案部分进行最后一次出堆即可得到第k小元
难点部分：

对于堆的构建
本题是两个序列类型，基于两个序列构建堆
堆内存放的元素为一个元祖，（元素和，第一个元素在第一个序列中的位置，第二个元素在第二个序列中的位置）
双序列类型问题要善于基于双序列元素位置设变量
'''