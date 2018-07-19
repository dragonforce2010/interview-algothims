'''
Given a matrix of lower alphabets and a dictionary. Find all words in the dictionary that can be found in the matrix. A word can start from any position in the matrix and go left/right/up/down to the adjacent position. One character only be used once in one word.

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
    def wordSearchII(self, board, words):
        if not board or not words:
            return []

        m, n = len(board), len(board[0])
        self.visited = set()
        self.dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
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

'''
又一道新题，最近LeetCode出现新题的速度略快啊。刚看到题目想到之前有一道Word Search，所以马上想到暴力搜索每一个单词，但是很不幸跟预想的一样超时了，看了一下hint，提到了字典树。所以先用所给的单词来构建字典树，然后在dfs搜索字典树中的单词，这样就避免了大量的重复比较。另外如果搜索的路径已经不是字典树是的前缀了就可以直接剪枝返回了。下面是AC代码。因为要避免重复，我先用了一个set存结果，然后再转存到result中。
解题思路：
将待查找的单词储存在字典树Trie中，使用DFS（深度优先搜索）在格板中查找，利用字典树剪枝。
每当找到一个单词时，将该单词从字典树中删去。
返回结果按照字典序递增排列。
哈希表在此题中不适用，因为单词前缀的存储会消耗大量的空间。
'''