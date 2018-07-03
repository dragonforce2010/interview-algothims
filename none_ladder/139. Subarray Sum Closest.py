'''
Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

Example
Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

Challenge
O(nlogn) time
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    #使用全局常量表示常数，而不要用局部变量
    MIN_DIST = 890981321
    
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []

        # 初始化前缀和数组，i从第0个位置一直到第n个位置
        # 注意：我们将前缀和的时候使用的是位置的概念，而且我们容纳了位置0处的前缀和的表示，所以总共有n + 1个前缀和        
        # 位置0处的前缀和为0
        # 我们放入前缀和数组中的元素是一个元组，因为我们除了记录前缀和，还想记录位置(不是下标)
        presum = [(0, i) for i in range(len(nums) + 1)]
        # 使用for循环计算从位置1到位置n处的前缀和
        for index in range(1, len(nums) + 1):
            sum, _ = presum[index - 1]
            presum[index] = (sum + nums[index - 1], index)
        
        presum.sort()
        minDist = Solution.MIN_DIST
        ansl, ansr = 1, 1
        
        # 从位置1到位置n，计算每个位置的前缀和与其前一个位置的前缀和的距离，并且更新全局最小距离
        for index in range(1, len(nums) + 1):
            dist =  presum[index][0] - presum[index - 1][0]
            if dist < minDist:
                minDist = dist
                ansl = min(presum[index][1], presum[index - 1][1]) + 1
                ansr = max(presum[index][1], presum[index - 1][1])
        # 因为我们最后返回下标，所以需要减去1 
        return [ansl - 1, ansr - 1]