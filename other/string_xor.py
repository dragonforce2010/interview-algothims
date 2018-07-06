class Solution:
    def sxor(self, str1, str2):
        if not str1 or not str2:
            return None
        
        return ''.join([(a + b) if (ord(a) ^ ord(b)) else '' for a, b in zip(str1, str2)])

'''Test'''
solution = Solution()
result = solution.sxor('abbc', 'abbc')
print(result)