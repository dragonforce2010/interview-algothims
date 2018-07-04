'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
'''
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        
        # sort the array, important!
        nums.sort()
        res, length = [], len(nums)
        for i in range(0, length - 2):
            # remove the duplicates
            if i and nums[i] == nums[i - 1]:
                continue
            
            # fix nums[i] element, then problem becomes two sum in the remaining array
            target = -nums[i]
            # two pointers
            left, right = i + 1, length - 1
            while left < right:
                # calculate two sum, based on the comparasion with target, we adjust/update left/right pointer
                value = nums[left] + nums[right]
                if value == target:
                    res.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    # remove the duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # remove the duplicates
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif value > target:
                    right -= 1
                else:
                    left += 1
        return res

'''
算法武器：双指针(对冲型)
时间复杂度：O(n^2+nlogn)=(n^2)

算法思路：

数组排序
利用2sum思路，首先使用一个for循环固定一个元素num[i]（下标取值范围在[0, len - 3]），然后将其变成在数组中寻找2sum的问题
将target定义为-num[i], 定义双指针，分别指向i+1和最右lenght - 1,开始进行2sum求解
注意：
-首先对数组进行排序

在第一层for循环中需要对固定的元素nums[i]进行去重，因为固定相同的元素只能得到相同的结果
在第二层for循环中，在找到解之后我们需要更新left和right指针，同时还要去重
'''