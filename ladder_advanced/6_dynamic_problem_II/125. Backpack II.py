'''Description
Given n items with size Ai and value Vi, and a backpack with size m. What's the maximum value can you put into the backpack?

 Notice
You cannot divide item into small pieces and the total size of items you choose should smaller or equal to m.

Have you met this question in a real interview? 
Example
Given 4 items with size [2, 3, 5, 7] and value [1, 5, 2, 4], and a backpack with size 10. The maximum value is 9.

Challenge 
O(n x m) memory is acceptable, can you do it in O(m) memory?
'''
class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A & V: Given n items with size A[i] and value V[i]
    # @return: The maximum value
    def backPackII(self, m, A, V):
        # write your code here
        f = [0] * (m+1)
        # for i in range(len(A)):
        #     for j in range(m, A[i] - 1, -1):
        #         if f[j] < f[j - A[i]] + V[i]:
        #             f[j] = f[j-A[i]] + V[i]
        for j in range(0, m + 1):
            for i in range(len(A)):
                if j >= A[i] and f[j] < f[j - A[i]] + V[i]:
                    f[j] = f[j-A[i]] + V[i]
        return f[m]
'''Summary
和背包问题1的区别是：
背包1给定一个体积的上限，物品体积列表，要求我们装入最大的物品体积
背包2给定一个体积的上限，物品体积列表，和背包物品value列表，要求我们装入最大的value

本题解法分析：
f[i]: 代表当体积上限是i时，我们能够装入背包的最大价值
答案：f[m], 即当背包体积上限是m时，我们能够装入的最大价值

心得：体积上限是限制性因素，我们可以把限制性因素放在dp数组的下标中
'''