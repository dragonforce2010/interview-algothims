'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
'''
class Solution:
    """
    @param nums: an array
    @return: the Next Greater Number for every element
    """
    '''
    - 简单解法，使用暴力循环每个元素
    - 注意，因为本题允许循环扫描，那么我们的解法是内部的cursor j的取值是从i -》 i + len(nums）,这样我们保证从i开始的元素能够循环扫描整个数组
    - 注意使用%运算
    - 注意使用for else语句简化程序编写
    '''
    def nextGreaterElements1(self, nums):
        if not nums:
            return []
            
        length = len(nums)
        monoStack = []
        # 我们开辟了一个length长度的数组，而不是使用动态方式表示[],因为我们想动态更新我们的result
        # 当我们扫描到循环部分的时候，我们通过result[i % length] = monoStack[-1] 来更新result
        result = [-1] * length
        
        # 我们使用重复（拼接）的方式来化解循环数组带来的复杂情况
        # 注意我们
        for i in range(length * 2 - 1, -1, -1):
            while monoStack and nums[i % length] >= monoStack[-1]:
                monoStack.pop()

            # 注意我们对result的更新是通过i%length这种形式表示的    
            if not monoStack:
                result[i % length] = -1
            else:
                result[i % length] = monoStack[-1]
                
            monoStack.append(nums[i % length])
        
        return result

    def nextGreaterElements2(self, nums):
        # Write your code here
        if not nums:
            return []
            
        result = []
        for i in range(len(nums)):
            for j in range(i, i + len(nums)):
                if nums[ j % len(nums)] > nums[i]:
                    result.append(nums[j % len(nums)])
                    break
            else:
                result.append(-1)
                
        return result
