'''Description
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only upper and lower case letters (a-z).

'''

class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, string):
        # 处理长度小于等于1的情形
        if len(string) <= 1:
            return string
            
        result = []
        # 因为在扫描过程中我们需要知道当前扫描字符和前一个被扫描字符
        # 所以这里使用prev和curr两个变量
        prev, curr = None, string[0]
        
        # 长度初始化为1，不是0哦
        count = 1
        for i in range(1, len(string)):
            # 访问每个个字符时，首先更新prev和curr
            prev, curr = curr, string[i]
            
            # 判断当前项是否等于前项， 是则继续计数
            if curr == prev:
                count += 1
                continue
            else: # 否则进行输出
                if count > 1:
                    result.append(prev + str(count))
                else:
                    result.append(prev * count)
                # 重置count
                count = 1
        
        # 边界处理，注意使用curr，而不是prev        
        if count > 1:
            result.append(curr + str(count))
        else:
            result.append(curr)
                
        return ''.join(result)

class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    def compress(self, string):
        # 处理长度小于等于1的情形
        if len(string) <= 1:
            return string
            
        result = []
        # 因为在扫描过程中我们需要知道当前扫描字符和前一个被扫描字符
        # 所以这里使用prev和curr两个变量
        prev, curr = None, string[0]
        
        # 长度初始化为1，不是0哦
        count = 1
        for i in range(1, len(string)):
            # 访问每个个字符时，首先更新prev和curr
            prev, curr = curr, string[i]
            
            # 判断当前项是否等于前项， 是则继续计数
            if curr == prev:
                count += 1
                continue
            else: # 否则进行输出
                if count > 1:
                    result.append(prev + str(count))
                else:
                    result.append(prev * count)
                # 重置count
                count = 1
        
        # 边界处理，注意使用curr，而不是prev        
        if count > 1:
            result.append(curr + str(count))
        else:
            result.append(curr)
                
        return ''.join(result)

