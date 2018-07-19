'''
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.
Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.
'''
import heapq
class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        if heights == []:
            return 0
            
        m, n = len(heights), len(heights[0])
        visited = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        offsets = [ (-1, 0), (0, -1), (1, 0), (0, 1) ]
        
        # Get the boundary.
        min_heap = [] # A priority queue
        
        #put col 0 and col n - 1 into min_heap
        for i in range(m):
            heapq.heappush(min_heap, (heights[i][0], i, 0))
            visited[i][0] = 1
            
            heapq.heappush(min_heap, (heights[i][n-1], i, n-1))
            visited[i][n-1] = 1
        
        # put row 0 and row m - 1 into min_heap    
        for i in range(n):
            heapq.heappush(min_heap, (heights[0][i], 0, i))
            visited[0][i] = 1
            
            heapq.heappush(min_heap, (heights[m-1][i], m-1, i))
            visited[m-1][i] = 1
            
        # Start from the current shortest among the ones in the queue.
        # This ensures that a point would be explored from the LOWEST point around it!
        total_water = 0
        while min_heap:
            h, x, y = heapq.heappop(min_heap)
            for dx, dy in offsets:
                new_x =  x + dx 
                new_y = y + dy
                if 0 <= new_x < m \
                   and 0 <= new_y < n \
                   and not visited[new_x][new_y]:
                    if heights[new_x][new_y] < h:
                        total_water += h - heights[new_x][new_y]
                        
                    new_h = max(h, heights[new_x][new_y])
                    heapq.heappush(min_heap, (new_h, new_x, new_y))
                    visited[new_x][new_y] = 1
                        
        return total_water
'''
算法武器：堆（基于二维矩形）+ 访问数组

算法思路：

先把二维矩形四条边入堆
入堆的元素是一个三元组(当前维护的最大外围高度，入堆元素的row，入堆元素的col)
然后从外围高度最小的点开始出堆，这个最小的高度决定整个灌水的基调，这个可以借鉴一维灌水题目
入堆元素的坐标可以让我们访问到该元素的柱子高度，该高度和外围最大元素高度之差就是我们能够灌水的量
每次出堆一个元素时，这个元素一定外围中的最小高度，我们计算完它的灌水量之后，我们都把它周围的元素入堆
使用访问数组，防止元素被重新入堆
关于灌水的时机：

堆中存放的元素初始时是边界元素，这些边界元素不能灌水
当我们把该边界元素取出，我们检查它的邻居，对于每个邻居我们可以检测其是否能够盛水（只有邻居高度小于边界高度时才可以盛水）
h > heights[new_x][new_y]
邻居盛完水之后需要更新边界高度，并且将其push到堆中
邻居入堆之后标记其为被访问过，防止下次被重复入堆
等到下一次该元素被从堆里取出时，我们知道它的灌水量已经被计算过了，所以我们还是将其邻居节点找出来，然后计算每个邻居的盛水量，然后更新边界，将其推入堆中
简而言之：只有从堆中取出元素的有效的邻居才能够灌水
'''
