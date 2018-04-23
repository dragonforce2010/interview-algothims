'''Description
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return -1 instead.
Example
Given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

Challenge 
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        if not nums:
            return -1
            
        start, end = 0, 0
        length, sum, result = len(nums), 0, len(nums) + 1
        
        for start in range(length):
            while end < length and sum < s:
                sum += nums[end]
                end += 1
                
            if sum >= s:
                result = min(result, end - start)
                print(start, end - 1)
                
            sum -= nums[start]
            
        if result == len(nums) + 1:
            return -1
            
        return result

'''Summary
算法武器：双指针（不回溯）

本题的类型是窗口类 + 窗口尺寸不固定+双指针移动型

思路：
start变量用于代表窗口的起点，其值可以在[0, n- 1]
end变量代表窗口的终点，在for循环中我们使用while来尝试寻找相对于起点为start的end的位置
while循环中的条件包括对end的边界约束以及根据题目的要求的约束（本题中这个约束为子数组的和>=s）
循环跳出时我们需要对条件做检测，如果符合本题条件我们就更新解
更新窗口和，然后start指针随着for循环自动加1
本题的算法复杂度为O(n),因为所有元素都只被访问了2次（i一次，j一次）
虽然是嵌套的两个循环，但是因为两个指针都是一直向前走，没有回溯，所以时间复杂度可以维持在O(n)
'''