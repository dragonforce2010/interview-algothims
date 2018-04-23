'''Descript: 

Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number. The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Notice
Note that 1 is typically treated as an ugly number.
'''


import heapq

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.

    丑数计算过程：
    1
    2, 3, 5
    4, 6, 10,   6, 9, 15,    10, 15, 25

    """
    def nthUglyNumber(self, n):
        # write your code here
        if n <= 1:
            return n
            
        factors = [2, 3, 5]
        ugly_numbers = factors + [1]
        heap = heapq.heapify(ugly_numbers)
        
        count = 0
        while count < n - 1:
            ugly_num = heapq.heappop(ugly_numbers)
            count += 1
            for factor in factors:
                n_ugly_num = ugly_num * factor
                if n_ugly_num not in ugly_numbers:
                    heapq.heappush(ugly_numbers, n_ugly_num)
            
        return heapq.heappop(ugly_numbers)

'''Summary
算法武器：heap
求nth元素这类问题，我们一般都使用堆。使用堆时我们可以固定堆的大小比如为k，或是不固定大小，两种不同方式下的解题模板不同。

如果固定堆的大小为k，那么我们出堆一次，堆顶元素就是我们要求的kth元素
如果不固定堆的大小，那么我们一般用一个while循环连续出堆k - 1次，返回结果部分我们再出一次堆就是我们要求的结果。

这道题是之前那道Ugly Number 丑陋数的延伸，这里让我们找到第n个丑陋数，还好题目中给了很多提示，基本上相当于告诉我们解法了，根据提示中的信息，我们知道丑陋数序列可以拆分为下面3个子列表：
(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
仔细观察上述三个列表，我们可以发现每个子列表都是一个丑陋数分别乘以2,3,5，而要求的丑陋数就是从已经生成的序列中取出来的，我们每次都从三个列表中取出当前最小的那个加入序列，请参见代码如下：

def nthUglyNumber(self, n):
        # 判断边界条件,如果=1，则就返回1，因为1是丑数
        if n <= 1:
            return n

        # factors存放的是丑数主因子
        factors = [2, 3, 5]

        # 这是我们的堆，存放丑数
        # 将四个丑数放入堆中
        # 注意丑数3个因子就是三个丑数！！！
        # 注:python可以对元祖进行排序，默认排序规则是按元祖中的第一个数，然后按第二个数
        heap = factors + [1]
        import heapq
        heapq.heapify(heap)

        # 注意这里的n大于1是结束条件，这样保证我在返回时再出一次堆就是最终结果
        while n > 1:
            # 取出最小丑数，然后依次乘以丑数因子，再将其入堆
            uglyNum = heapq.heappop(heap)
            # 每次出堆依次，我们把n-1    
            n -= 1
            # level 取值在0 ~ 2之间
            for factor in factors:
                nUglyNum = factor * uglyNum
                # 注意：这里一定要剔除相同的元素，保证我们放入堆中的元素是不同的
                if nUglyNum not in heap:
                    heapq.heappush(heap, nUglyNum)
        return heapq.heappop(heap)

'''