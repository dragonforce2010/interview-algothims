'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Trapping Rain Water

Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory

O(n) time and O(n) memory is also acceptable.
'''
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
            
        left, right = 0, len(heights) - 1
        leftheight, rightheight = heights[left], heights[right]
        res = 0
        while left < right:
            if leftheight < rightheight:
                left += 1
                if leftheight > heights[left]:
                    res += leftheight - heights[left]
                else:
                    leftheight = heights[left]
            else:
                right -= 1
                if rightheight > heights[right]:
                    res += rightheight - heights[right]
                else:
                    rightheight = heights[right]
                    
        return res
'''
算法武器：左右相向型双指针
本题需要首先分析实验现象，然后归纳出解决问题的逻辑方法，然后着手编程。

我们通过实验发现，如果从左往右灌水，只有下一个柱子的高度比左边当前最大柱子高度小的时候，我们才能灌水。同理右边也是如此。

接下来的问题是怎么灌水？从哪个方向？从左边灌水？从右边灌水？一起灌水？
我们通过分析发现我们必须从左右两边中高度最小的一边开始灌水，这样我们保证水不会漏掉。如果出现漏水现象，那么是因为水往高度更低的地方留了，所以我们必须从左右两边边界柱子最低的位置开始。

因为柱子的高度不一，所以我们左右两边边界柱子的高度是在不断变化的，所以我们需要随时更新边界柱子高度。
'''