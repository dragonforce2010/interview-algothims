'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge
O(n^2) time, O(1) extra space
'''
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest1(self, numbers, target):
        numbers.sort()
        ans = sys.maxint
        for i in range(len(numbers) - 2):
            l, r = i + 1, len(numbers) - 1
            while l < r:
                sum = numbers[l] + numbers[r] + numbers[i]
                if abs(sum- target) < abs(ans - target):
                    ans = sum
                if sum <= target:
                    l = l + 1
                else:
                    r = r - 1
        return ans
        
    # 
    def threeSumClosest(self, numbers, target):
        if not numbers:
            return sys.maxint
            
        numbers.sort()
        ans = sys.maxint
        for i in range(len(numbers) - 2):
            l, r = i + 1, len(numbers) - 1
            while l < r:
                sum = numbers[i] + numbers[l] + numbers[r]
                if abs(sum - target) < abs(ans - target):
                    ans = sum
                if sum < target:
                    l += 1
                else:
                    r -= 1
        return ans

'''
算法武器： 排序 + 双指针（对冲型） + 固定一个变量
时间复杂度：O(n^2)
空间复杂度：O(1)

本题是2sum的难度加强版3sum，我们通过固定一个元素，将问题转化为2sum问题。当然对于固定的元素，我们需要枚举，使用一个for循环。
'''