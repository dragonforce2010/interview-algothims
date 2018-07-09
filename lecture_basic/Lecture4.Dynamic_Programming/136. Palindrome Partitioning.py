'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example
Given s = "aab", return:

[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s):
        # 存放全局结果
        self.res = []
        # 深搜
        self.dfs(s, [])
        # 返回结果
        return self.res
    
    # 搜索string s中的回文串划分，将其加入局部方案stringlist，然后放入全局结果中
    # 传入的子串s是越来越小的，直到传入的子串是空，则结束
    def dfs(self, s, stringlist):
        # 递归结束条件
        if not s:
            # 注意这里将局部切分方案的克隆返回
            self.res.append(stringlist[:])
            return
        
        # 遍历串s中的每一个切分位置，位置从[1-len(s)]
        # 注意切分位置从1开始s[:1]代表s[0],不包含s[1]
        for i in range(1, len(s) + 1):
            # 如果在i处切分，前i个字符是回文串，将该回文串加入局部切分方案列表，同时递归深搜后一个字符串的回文串的切分方案
            if self.isPalindrome(s[:i]):
                stringlist.append(s[:i])
                self.dfs(s[i:], stringlist)
                # 回溯
                stringlist.pop()

    # 判断是否一个串是回文串：字符收尾对称位置处需相等
    def isPalindrome(self, s):
        # 注意i的范围是从起点走到中间len(s) / 2即可
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        
        return True

'''
算法武器：深度优先搜索
算法思想：
定义全局结果变量，self.res
对给定字符串进行深度优先搜索，找出所有可行解，将其放入全局结果集中
dfs的每一个局部可行解使用局部变量保存，满足条件后加入到全局结果集
dfs函数职能：对输入字符串遍历所有可能的切分位置[1,length],没找到一个可行的切分位置即从字符串开始到当前位置是一个回文串，将这个回文串加入局部变量，然后递归求解。
每尝试一个位置，等递归函数返回时，我们需要进行回溯
注意：

在递归过程中对递归函数局部变量做的所有操作都需要回溯，以保证上层调用者的引用参数不会被被调用者改变
在for循环中，只要递归和回溯做完，这个for循环的主体就完成了
这又是一道需要用DFS来解的题目，既然题目要求找到所有可能拆分成回文数的情况，那么肯定是所有的情况都要遍历到，对于每一个子字符串都要分别判断一次是不是回文数，那么肯定有一个判断回文数的子函数，还需要一个DFS函数用来递归，再加上原本的这个函数，总共需要三个函数来求解
'''