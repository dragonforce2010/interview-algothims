'''Description
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

 Notice
If the element in the given list is a list, it can contain list too.
Example
Given [1,2,[1,2]], return [1,2,1,2].

Given [4,[3,[2,[1]]]], return [4,3,2,1].

Challenge 
Do it in non-recursive.
'''
class Solution(object):
    
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    
    # Recursive solution
    def flatten(self, nestedList):
        # Write your code here
        # Termination condition
        if isinstance(nestedList, int):
            return [nestedList]

        result = []
        for ele in nestedList:
            result.extend(self.flatten(ele))

        return result
'''Summary
算法武器：递归
'''