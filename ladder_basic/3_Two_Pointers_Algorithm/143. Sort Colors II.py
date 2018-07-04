'''
Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example
Given colors=[3, 2, 2, 1, 4], k=4, your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?
'''
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        for i in xrange(len(colors)):
            if colors[i] > 0:
                while colors[colors[i]-1] > 0 and colors[i] != i+1 and \
                      colors[i] != colors[colors[i]-1]:
                    tmp = colors[i]
                    colors[i] = colors[colors[i]-1]
                    colors[tmp-1] = -1
                    
                if colors[i] == i+1:
                    colors[i] = -1
                elif colors[i] == colors[colors[i]-1]:
                    colors[colors[i]-1] = -2
                    colors[i] = 0
                else:
                    colors[colors[i]-1] -= 1
                    colors[i] = 0
                    
        i = len(colors)-1
        k = i
        while i >= 0:
            if colors[i] < 0:
                pos = k + colors[i]
                while k > pos:
                    colors[k] = i+1
                    k -= 1
            i -= 1