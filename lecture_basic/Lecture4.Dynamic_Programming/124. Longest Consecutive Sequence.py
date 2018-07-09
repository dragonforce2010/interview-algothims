'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
'''
class Solution:
    def longestConsecutive1(self, nums):
        if not nums:
            return -1

        dp = [1] * len(nums)
        nums.sort()

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] + 1 = nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    break
        
        return max(dp)

    def longestConsecutive2(self, nums):
        if not nums:
            return -1

        s, result = set(), 0

        for num in nums:
            s.add(num)

        for num in nums:
            if num in s:
                pre = num - 1
                next = num + 1
                s.remove(num)
                while pre in s:
                    s.remove(pre)
                    pre -= 1
                while next in s:
                    s.remove(next)
                    next -= 1

                result = max(result, next - pre - 1)

        return result

'''
算法武器：

数组扫描 O(n^2)
动态规划O(n^2)
算法1思想：
-创建一个set，用空间换区时间上O(n)效率

扫描一遍数组，考察每一个元素，计算其pre和next，用两个while循环持续寻找pre和next
每次考察完以当前元素为最长连续序列中的一个元素，计算最长长度，然后更新全局
所有元素都考察完一遍之后就获得了正确解
算法2思想：动态规划

本题和最长子序列有点像，区别在于本题强调连续
因为本题不关心原始序列的顺序，所以我们需要对原始序列排序（注意：不排序会少结果）
dp[i]: 以i作为最长连续序列结尾的序列的最大长度
使用两层for循环，内存for循环用于找到一个中间状态，使其和状态i建立关系，并且能够有可能更新状态i
max(dp)为答案返回，因为我们要求最长的连续序列，我们并不知道这个连续序列从哪里开始和从哪里结束，所以我们得选一个最大的
'''
                