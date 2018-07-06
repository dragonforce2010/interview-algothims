'''
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
'''
class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    '''
    使用简单解法：两重for循环，首先找到nums1元素在nums2数组中的位置，用标记变量found指示，然后扫描发现第一个找到的符合条件的元素，将其加入结果集
    注意：使用python的for else语法，当for循环完全结束的时候（中途没有break），那么else的部分会执行，如果中途有break，那么else的部分也会被break掉
    python的for else语法非常高级和方便，一定要学会使用
    '''
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        if not nums1 or not nums2:
            return []
        
        result = []
        
        for i in range(len(nums1)):
            # 初始化标记变量
            found = False
            for j in range(len(nums2)):
                if found and nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    break
                
                #控制更新标记变量
                if nums2[j] == nums1[i]:
                    found = True
            else:
                result.append(-1)
                
        return result

    # use monontone stack
    def nextGreaterElement(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
            
        # 声明单调栈    
        monoStack = []
        # 存放从右往左扫描，每一个元素的向右延伸的第一个比它大的元素
        eleGreaterMap = {}
        # 返回结果
        result = []
        for i in range(len(nums2) - 1, -1, -1):
            # 每一个元素放入栈之前需要对栈进行调整，如果元素破坏了栈的单调性，那么我们需要对栈里元素逐一pop，
            # 直到当前元素找到了它在栈中的位置
            # 注意这里使用的是while，我们需要一直不断地调整栈，知道栈单调
            while monoStack and nums2[i] > monoStack[-1]:
                monoStack.pop()
                
            # 如果栈在调整之后变空，那么代表当前元素向右延伸找不到比它大的元素，我们将其结果记为-1
            if not monoStack:
                eleGreaterMap[nums2[i]] = -1
            # 否则栈顶元素就是答案
            else:
                eleGreaterMap[nums2[i]] = monoStack[-1]
            
            # 将当前元素入栈
            monoStack.append(nums2[i])

        # 扫描数组1，找到对应的结果    
        for ele in nums1:
            result.append(eleGreaterMap[ele])
            
        return result
                