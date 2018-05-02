'''Description
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the median of the element inside the window at each moving. (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )
Example
For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]

At first the window is at the start of the array like this

[ | 1,2,7 | ,8,5] , return the median 2;

then the window move one step forward.

[1, | 2,7,8 | ,5], return the median 7;

then the window move one step forward again.

[1,2, | 7,8,5 | ], return the median 7;

Challenge 
O(nlog(n)) time
'''
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of element inside the window at each moving.
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or k < 0 or k > len(nums):
            return []
            
        res = []
        for i in range(len(nums) - k + 1):
            # print(sorted(nums[i : i + k]))
            median = sorted(nums[i : i + k])[(k - 1) / 2]
            res.append(median)
            
        return res
'''Summary
解法2：该解法不能通过时间复杂度，不过可以借鉴一下
def medianSlidingWindow(self, nums, k):
        if not nums or k < 0 or k > len(nums):
            return []

        res = []
        # 注意i作为窗口的起点下标，终点下标可以到达len(nums - k)
        for i in range(len(nums) - k + 1):
            # 我们求窗口区间的数组段是：nums[i:i + k]
            # 求中位数的下标是(k - 1) / 2
            median = sorted(nums[i : i + k])[(k - 1) / 2]
            res.append(median)

        return res
'''