'''Description:
Count the number of k's between 0 and n. k can be 0 - 9.

Example
if n = 12, k = 1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
we have FIVE 1's (1, 10, 11, 12)
'''

class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """

    def digitCounts(self, k, n):
        # write your code here
        assert(n >= 0 and 0 <= k <= 9)
        count = 0
        for num in range(n + 1):
            digits = num
            # 对每个数字的每一位的遍历使用的是取余除10法
            while True:
                if digits % 10 == k:
                    count += 1
                # /: 返回float类型数字
                # //: 返回整数
                digits //= 10
                if digits == 0:
                    break
        
        return count