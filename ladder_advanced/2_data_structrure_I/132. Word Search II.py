'''Description
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. 
Example
Given matrix:

doaf
agai
dcan
and dictionary:

{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}


dog:
doaf
agai
dcan
dad:

doaf
agai
dcan
can:

doaf
agai
dcan
again:

doaf
agai
dcan
Challenge 
Using trie to implement your algorithm.
'''

class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []
            
        m, n = len(board), len(board[0])
        self.visited = set()
        self.dirs = [
            (0, 1),  # up 
            (1, 0),  # right
            (0, -1), # down
            (-1, 0)  # left
        ]
        self.result = []
        self.trie = self.initTrie(words)
        
        for x in range(m):
            for y in range(n):
                if self.trie.root.children.get(board[x][y]):
                    self.visited.add((x, y))
                    self.dfs(board, self.trie.root, board[x][y], x, y)
                    self.visited.remove((x, y))
                
        return self.result
        
        
    def dfs(self, board, trieNode, word, x, y):
        if not trieNode:
            return 
        
        curNode = trieNode.children.get(board[x][y])
        if curNode is None:
            return
        
        if curNode.isWord:
            self.result.append(word)
            self.trie.delete(word)
            
        for dx, dy in self.dirs:
            nx = x + dx
            ny = y + dy
            if self.validate(board, nx, ny):
                self.visited.add((nx, ny))
                self.dfs(board, curNode, word + board[nx][ny], nx, ny)
                self.visited.remove((nx, ny))
                
    def validate(self, board, x, y):
        m, n = len(board), len(board[0])
        if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in self.visited:
            return True
            
        return False
        
    def initTrie(self, words):
        root = TrieTree()
        if not words:
            return root
        
        for word in words:
            root.insert(word)
            
        return root
        
#***************************************************************************
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
class TrieTree:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        curNode = self.root
        for letter in word:
            child = curNode.children.get(letter)
            if not child:
                child = TrieNode()
                curNode.children[letter] = child
            curNode = child
        
        curNode.isWord = True
        
        
    def delete(self, word):
        if not word:
            return
        
        curNode = self.root
        queue = []
        for ch in word:
            queue.append((ch, curNode))
            child = curNode.children.get(ch)
            if not child:
                return
            curNode = child
        
        if not curNode.isWord:
            return
        
        if curNode.children:
            curNode.isWord = False
            return
        
        for letter, node in reversed(queue):
            del node.children[letter]
            if node.children or node.isWord:
                break
 '''Summary
 又一道新题，最近LeetCode出现新题的速度略快啊。刚看到题目想到之前有一道Word Search，所以马上想到暴力搜索每一个单词，但是很不幸跟预想的一样超时了，看了一下hint，提到了字典树。所以先用所给的单词来构建字典树，然后在dfs搜索字典树中的单词，这样就避免了大量的重复比较。另外如果搜索的路径已经不是字典树是的前缀了就可以直接剪枝返回了。下面是AC代码。因为要避免重复，我先用了一个set存结果，然后再转存到result中。
解题思路：
将待查找的单词储存在字典树Trie中，使用DFS（深度优先搜索）在格板中查找，利用字典树剪枝。
每当找到一个单词时，将该单词从字典树中删去。
返回结果按照字典序递增排列。
哈希表在此题中不适用，因为单词前缀的存储会消耗大量的空间。


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def wordSearchII(self, board, words):
        # write your code here
        self.board = board
        self.words = words
        self.w, self.h = len(board[0]), len(board)

        # 根据单词列表构建Trie树
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        # 构建矩阵的访问数组（初始化为False）
        self.visited = [[False] * self.w for x in range(self.h)]
        self.dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        # 保存答案
        self.ans = []

        # 遍历矩阵中的每一个点
        for x in range(self.h):
            for y in range(self.w):
                # 从当前点出发深度搜索
                self.visited[x][y] = True
                self.dfs(board[x][y], self.trie.root, x, y)
                self.visited[x][y] = False

        # 返回排序后的ans
        return sorted(self.ans)

    # 从x,y点出发，深度搜索、探测单词
    # curNode是trie树的树根
    def dfs(self, word, curNode, x, y):
        # 递归的结束条件
        # 如果以字符board[x][y]开始的单词不存在于trie树root中，那么该递归调用结束
        curNode = curNode.childs.get(self.board[x][y])
        if curNode is None:
            return

        # 判断当前节点是否是个单词，如果是则加入答案中
        if curNode.isWord:
            self.ans.append(word)
            # 在trie树种删除该单词，以去重
            self.trie.delete(word)

        #如果存在，则标记该点被访问过
        # 从该点开始，探索其四个方向
        for z in self.dz:
            nx, ny = x + z[0], y + z[1]
            # 检测新的点的合法性：在界限范围内，并且没有被访问过            
            if nx >= 0 and nx < self.h and ny >= 0 and ny < self.w and not self.visited[nx][ny]:
                # 深度递归搜索
                self.visited[nx][ny] = True
                self.dfs(word + self.board[nx][ny], curNode, nx, ny)
                self.visited[nx][ny] = False

# 构建Trie树节点数据结构
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False

# 构建Trie树
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    # Trie树的插入
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    # Trie树的删除
    def delete(self, word):
        node = self.root
        queue = []
        # 遍历单词中的每个字符
        for letter in word:
            # 将元祖(letter, node)放入队列
            queue.append((letter, node))
            child = node.childs.get(letter)
            # 如果单词不在Trie树中就直接返回False，不用做任何其他操作
            if child is None:
                return False
            # 当前Trie树节点后移    
            node = child
        # 当循环退出时，node指向单词最后一个字符的Trie树节点
        # 如果该节点不是word，那么不用做任何操作，直接返回False
        if not node.isWord:
            return False
        # 如果该Trie树节点还有孩子，那么只将其单词标志置为False完成删除操作    
        if len(node.childs):
            node.isWord = False
        # 如果该节点没有孩子节点，那么要一次从下至上删除Trie树节点    
        else:
            # 以逆序顺序取出单词和节点
            for letter, node in reversed(queue):
                # 删除该Trie树节点中对应letter的孩子，删除字典中的记录
                del node.childs[letter]
                # 如果该节点孩子数目为不为0，或者该节点是一个单词，那么终止操作
                if len(node.childs) or node.isWord:
                    break
        return True
'''