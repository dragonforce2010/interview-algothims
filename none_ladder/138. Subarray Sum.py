'''
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if not nums:
            return []

        # 使用presum对当前[0, index]的前缀和进行计算
        # - 如果前缀和为0，这是一种特殊情况，我们直接返回[0, index]，就不用查hashmap了
        # - 如果前缀和在hashmap中，那么我们就找到了两个有相同值得前缀和，根据推理，和为0的子区间就是[hashmap[presum] + 1, index]
        #   这个是基于公式presumeArr[i + 1, j] = presumArr[j] - presumArr[i]
        #   注意，上面的公式使用了前缀和数组，但本题比较简单我们不需要计算和保留前缀和数组（其实某种程度上也算是保留了，因为我们把前缀和都存在了hashmap中）
        #   本题直接使用滚动更新的前缀和presum来进行计算
        # - 如果我们没有在hashmap中找到前缀和，那么我就将当前前缀和推入到hashmap 
        presum, hashmap = 0, {}
        for index, num in enumerate(nums):
            presum += num
            if presum == 0:
                return [0, index]
                
            if presum in hashmap:
                return [hashmap[presum] + 1, index]
            else:
                hashmap[presum] = index
                
        return []