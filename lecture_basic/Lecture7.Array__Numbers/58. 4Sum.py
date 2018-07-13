'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Example
Given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''
class Solution:
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []

        nums.sort()
        res, length = [], len(nums)

        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                if j > i and nums[j] == nums[j - i]:
                    continue

                sum = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1

        return res