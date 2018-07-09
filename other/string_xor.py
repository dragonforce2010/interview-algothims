class Solution:
    def sxor(self, str1, str2):
        if not str1 or not str2:
            return None
        
        return ''.join([(a + b) if (ord(a) ^ ord(b)) else '' for a, b in zip(str1, str2)])

    def sxor2(self, str1):
        if not str1:
            return None

        

'''Test'''
solution = Solution()
result = solution.sxor('abbc', 'abbc')
print(result)