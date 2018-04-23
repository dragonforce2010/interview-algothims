'''Descript
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode
'''

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        return ''.join(['%d$%s' % (len(word), word) for word in strs])

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, s):
        # write your code here
        result, start = [], 0
        while start < len(s):
            index = s.find('$', start)
            word_length = int(s[start:index])
            start = index + 1 + word_length
            result.append(s[index + 1:start])
            
        return result

solution = Solution()
encoded_string = solution.encode(['I', 'love', 'lint', 'code'])
decoded_str_arr = solution.decode(encoded_string)


'''Summary
掌握python的string操作函数
''.join('%d$' % len(s) + s for s in strs)
s.find('$', i)

掌握字符串编码和解码的基本方法
编解码的重要作用是能够区分传输的每个单词

本题使用的是通过编码长度和编码标记$符号来完成编码，通过编码标记能够找到编码长度，通过编码长度能够正确取出编码的字符。
注：即使编码单词中含有编码标记也没有关系，因为编码长度能够帮我们取到正确的编码单词，同时我们在下一次寻找编码标记$时，我们会跳过已经找过的单词，这样单词的内容就不会影响我们的解码
'''
