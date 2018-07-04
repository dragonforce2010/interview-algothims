class Solution：
    def longestPalindrome(self, s):
        ansl, ansr, maxx = 0, 1, 0
        length = len(s)

        for i in range(length * 2):
            if i & 1:
                left = i / 2
                right = left
            else:
                left = i / 2 - 1
                right = left + 1
            
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            
            left += 1
            right -= 1
            if right - left + 1 > maxx:
                maxx = right - left + 1
                ansl = left
                ansr = right

            return s[ansl: ansr + 1]