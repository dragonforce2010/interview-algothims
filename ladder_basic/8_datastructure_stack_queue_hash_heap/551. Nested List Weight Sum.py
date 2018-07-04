'''
Given a nested list of integers, return the sum of all integers in the list weighted by their depth. Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example
Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1, 4 * 1 * 2 + 1 * 2 * 1 = 10)
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)
'''


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    
    # Solution1: Using stack*******************************************
    def depthSum(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0
            
        stack = []
        sum = 0
        for n in nestedList:
            # scan and initialized the stack seed elements, mark the current depth to be 1
            stack.append((n, 1))
        
        # loop through the stack and only process the simplest situation, otherwise just push to the stack for further process
        while stack:
            elem, depth = stack.pop()
            # if it's integer, then caculate
            if elem.isInteger():
               sum += depth * elem.getInteger()
            else: # otherwise, scan and push to the stak and increase the depth
                for nextElem in elem.getList():
                    stack.append((nextElem, depth + 1))
        return sum
        
    #Solution2: Using Queue*******************************************
    def depthSum2(self, nestedList):
        # Write your code here
        if not nestedList:
            return 0
            
        queue = collections.deque([])
        sum = 0
        for n in nestedList:
            queue.append((n, 1))
        
        while queue:
            elem, depth = queue.popleft()
            if elem.isInteger():
               sum += depth * elem.getInteger()
            else:
                for nextElem in elem.getList():
                    queue.append((nextElem, depth + 1))
        return sum

'''
算法武器：stack

本题要求嵌套list中元素的和，和的计算为元素 X 深度
stack非常适合解决嵌套类型的问题，基本思路如下：

扫描一遍嵌套list，将所有元素入栈
入栈的元素是一个元祖（元素，深度），我们需要深度变量计算sum
用while遍历stack，直到stack中的所有元素被处理完毕
对于从栈中pop出的每一个元素，如果该元素是非嵌套的，我们则可以直接计算累加sum
如果元素是嵌套的list，我们就遍历这个这个list元素，并且将其中的子元素再次入栈，让其等待下次处理（这一步其实我们队嵌套的list元素做了一个拆包）
while循环退出后，返回sum
本题用stack也好，还是queue也好，都可以获得求解，因为我们不关注处理的顺序。
stack和queue的好处是我们可以把元素首先放入stack/queue中，然后用while循环，逐一取出，逐一求解，对于处理不了的，我们就做初步拆包处理，然后放回，让其等待下次处理。
'''