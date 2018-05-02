'''Description
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example
Given height = [2,1,5,6,2,3],
return 10.
'''
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        stack, i, area =[], 0, 0 
        
        while i<len(height):
            if stack==[] or height[i]>height[stack[-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                # width = i if stack==[] else i-stack[len(stack)-1]-1
                width = i-stack[len(stack)-1]-1
                area = max(area, width * height[curr])
                i -= 1
            i+=1
            
        while stack!=[]:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[len(stack)-1]-1
            area=max(area,width*height[curr])
        return area

'''Summary
单调栈：http://fisherlei.blogspot.com/2012/12/leetcode-largest-rectangle-in-histogram.html
'''