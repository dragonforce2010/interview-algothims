'''Description
Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.
Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

Challenge 
Can you do it without recursion?
'''
class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        stack = []
        number = 0
        for char in s:
            # input: "10[abc]"
            # output: "abcabcabcabcabcabcabcabcabcabc"
            # input: "0[abc]"
            # ""
            if char.isdigit():
                number = number * 10 + ord(char) - ord('0')
            elif char == '[':
                stack.append(number)
                number = 0
            elif char == ']':
                strs = []
                while stack:
                    elem = stack.pop()
                    if type(elem) == int:
                        stack.append(''.join(reversed(strs)) * elem)
                        break
                    strs.append(elem)
            else:
                stack.append(char)
        return ''.join(stack)

'''Summary
算法武器：stack
根据题目分析，题目中含有嵌套这个概念，那么用栈解决再适合不过。

算法思路：
- 逐个字符扫描，处理遇到数字，"[", "]"和普通字符的情形
- 遇到数字：需要进行累加，因为我们可能连续遇到多个数字，累加时考虑10进制移位
- 遇到"[":需要把累加计算好的数字推到栈中，这个数字会被下一个子串表示时用到，这个数字是下一个子串的重复数目，因为下个子串我们还没扫到，所以当前的数字我们先保存在栈中，等到处理完子串的时候，再把它从栈中取出来使用
- 遇到"]"：表示一个子串已经扫描完毕，这是我们要把栈中的元素使用while循环一个一个取出来拼接出子串，直到在栈中遇到一个数子，这个数字代表该子串的重复数目。由于出栈的时候是逆序的，所以我们需要把元素reverse一下。当我们把这个子串重复的表示计算出之后，需要把它再放回栈中，因为这个新的大的子串可能会被重复表示
- 遇到普通字符的时候：直接进栈
- 返回栈中所有元素的字符串拼接

本题中的栈不仅使用了栈的特点：先进后出，同时还使用了栈保存数据元素。本题不是像其它类型的栈的题目使用一个while循环遍历栈中所有元素，知道栈中元素全部被处理完毕。本题的栈即对元素做处理，同时还保存数据，最后栈中的数据即为答案。
'''