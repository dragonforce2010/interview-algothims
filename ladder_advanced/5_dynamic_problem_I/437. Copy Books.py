'''Description
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books. For example one copier can copy the books from ith to jth continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books. For example one copier can copy the books from ith to jth continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the slowest copier can finish at earliest time?
'''
class Solution:
    # @param pages: a list of integers
    # @param k: an integer
    # @return: an integer
    def copyBooks(self, pages, k):
        if not pages or k <= 0:
            return 0
            
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.countCopier(pages, mid) > k:
                start = mid
            else:
                end = mid
        
        if self.countCopier(pages, start) <= k:
            return start
        else:
            return end

    def countCopier(self, pages, timeLimit):
        totalTime = 0
        totalCopier = 1
        for i in range(0, len(pages)):
            if totalTime + pages[i] > timeLimit:
                totalCopier += 1
                totalTime = 0
                
            totalTime += pages[i]
        
        return totalCopier
            
    
    # def copyBooks2(self, pages, k):
    #     n = len(pages)
    #     if (k>n): 
    #         k = n
        
    #     if n == 0:
    #         return 0
        
    #     sum = []
    #     for i in xrange(n): 
    #         sum.append(0)
        
    #     sum[0] = pages[0]
    #     for i in xrange(1, n): 
    #         sum[i] = sum[i-1] + pages[i]
        
    #     f = []        
    #     for i in xrange(n):
    #         f.append([])
    #         for j in xrange(k): 
    #             f[i].append(0)
        
    #     for i in xrange(n): 
    #         f[i][0] = sum[i]
            
    #     for j in xrange(1, k):
    #         p = 0
    #         f[0][j] = pages[0]
    #         for i in xrange(1, j): 
    #             f[i][j] = max(f[i-1][j], pages[i]) 
            
    #         for i in xrange(j, n):
    #             while (p<i and f[p][j-1] < sum[i] - sum[p]): 
    #                 p += 1
                
    #             f[i][j] = max(f[p][j-1], sum[i] - sum[p])               
                
    #             if (p>0): 
    #                 p -= 1
                
    #             f[i][j] = min(f[i][j], max(f[p][j-1], sum[i] - sum[p]))         
        
    #     return f[n-1][k-1]
'''Summary
算法武器：枚举思想 + 二分答案
算法思想：
- 本题可以大胆设定这个最慢拷贝者的时间（ slowest copier can finish at earliest time）为变量，然后枚举这个变量看是否合理
- 判断是否合理的方式是查看其是否满足本题约束条件：K个人能够完成任务
- 在枚举思想的基础之上我们使用二分法来加速枚举的效率
- 我们通常说的二分答案这种思想，其实和我们的枚举思想很有关联，我们先把我们要求的设置成变量，再二分枚举这个变量的可能值。

二分答案思想：对一个问题，我们知道问题解的范围，比如最大最小值，我们需要确定问题解，这种情况下我们可以使用二分答案法，在答案范围内二分搜索答案，对于每个二分的答案解，我们待会条件验证，如果满足条件，则我们可以进一步调整二分答案的区间，直到找到符合条件的最有解。

start初值是max，也就是有一本书，它的页码是所有书里面最大的，那么至少有一个人的时间会大于等于这本数的所需时间。
end初值是total，也就是所有页码的sum，意思就是如果只有一个人复印的话，需要的时间。因为这里的k是函数给定的，可能就是要求1个人。
在理解这个start和end的初值的基础上。
进行二分法的求解。countcopier确实没有返回，当前countcopier(pages, limit)的时候最慢的那个人需要的时间。但是我们并不需要知道这个最慢的人需要的时间。（最慢的这个人的时间，至少是大于等于start初值max的，而且最慢的这个人的时间是小于等于limit的）
情况1：当前limit的时间需要的人数小于等于k，说明limit这个时间可以完成任务，但是不一定是最短时间，所以end=limit把范围向下缩小。
情况2：当前limit的时间需要的人数大于k，说明limit这个时间不能完成任务，也就是limit太小了，需要的人太多了，所有小于limit的时间更不可能完成任务，于是start=limit，把二分范围向上缩小。
直到退出二分while循环。
这时就只存在两种可能了，如果start能完成任务，它就一定是最小的时间，否则就是end
'''