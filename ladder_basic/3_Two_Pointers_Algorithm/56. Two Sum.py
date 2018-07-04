'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

Example
numbers=[2, 7, 11, 15], target=9

return [0, 1]

Challenge
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
'''
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return [-1, -1]
            
        myhash = {}
        for index, num in enumerate(numbers):
            if target - num in myhash:
                return [myhash[target - num], index]
            
            myhash[num] = index
            
        return [-1, -1]
