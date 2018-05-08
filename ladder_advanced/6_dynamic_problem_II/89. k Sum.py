'''Description
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Have you met this question in a real interview? 
Example
Given [1,2,3,4], k = 2, target = 5.

There are 2 solutions: [1,4] and [2,3].

Return 2.
'''
class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        # write your code here
        ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(len(A) + 1)]
        
        ans[0][0][0] = 1
        for I in range(len(A)):
            item = A[I]
            for J in range(target + 1):
                for K in range(k + 1):
                    tk = k - K
                    tj = target - J
                    ans[I + 1][tk][tj] = ans[I][tk][tj]
                    if tk - 1 >= 0 and tj - item >= 0:
                        ans[I + 1][tk][tj] += ans[I][tk - 1][tj - item]
        return ans[len(A)][k][target]

'''Summary
http://www.cnblogs.com/yuzhangcmu/p/4279676.html
'''