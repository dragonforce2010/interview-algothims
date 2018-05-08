'''Description
Given a board which is a 2D matrix includes a-z and dictionary dict, find the largest collection of words on the board, the words can not overlap in the same position. return the size of largest collection.

 Notice
The words in the dictionary are not repeated.
You can reuse the words in the dictionary.
Example
Give a board below

[['a', 'b', 'c'],
 ['d', 'e', 'f'],
 ['g', 'h', 'i']]
dict = ["abc", "cfi", "beh", "defi", "gh"]
Return 3 // we can get the largest collection["abc", "defi", "gh"]
'''
class Solution:
    def boggleGame(self, board, words):
        if not board or not words:
            return 0
            
        m, n = len(board), len(board[0])
        self.maxCnt = 0
        self.dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]
        self.trie = Trie()
        self.trie.addWords(words)
        
        for x in range(m):
            for y in range(n):
                if self.trie.searchPrefix(board[x][y]):
                    visited = [[False] * n for _ in range(m)]
                    visited[x][y] = True
                    self.dfs(board, x, y, visited, 0, board[x][y])
                    
                    if self.maxCnt == m * n:
                        return self.maxCnt
                        
        return self.maxCnt
        
    
    '''
    def dfs(self, board, x, y, visited, cnt, word):
        m, n = len(board), len(board[0])
        if self.trie.search(word):
            # print(word)
            cnt += 1
            self.maxCnt = max(self.maxCnt, cnt)
            tempVisited = set()
            
            for i in range(m):
                for j in range(n):
                    if self.trie.searchPrefix(board[i][j]) and not visited[i][j]:
                        visited[i][j] = True
                        tempVisited.add((i, y))
                        self.dfs(board, i, j, visited, cnt, board[i][j])
            
            # å¨æ¬å±ä¸­ï¼æä»¬å¯¹visitedåäºéå¸¸å¤çä¿®æ¹ï¼è¿éè¿è¡éä½åæº¯ï¼åæº¯ä¹åå°±ç¸å½äºæä»¬æ²¡æéæ©è¿è¿ä¸ªåè¯ï¼æ¶é¤å¯¹åç»­æ¹æ¡çå½±å
            for x, y in tempVisited:
                visited[x][y] = False
            # print(visited)
        else:
            for dx, dy in self.dirs:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and not visited[nx][ny] and self.trie.searchPrefix(word + board[nx][ny]):
                    visited[nx][ny] = True
                    self.dfs(board, nx, ny, visited, cnt, word + board[nx][ny])
                    # print(word + board[nx][ny])
                    visited[nx][ny] = False

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
        
class Trie:
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
        
    
    def addWords(self, words):
        if not words:
            return
        
        for word in words:
            self.insert(word)
            
            
    def search(self, word):
        if not word:
            return False
            
        curNode = self.root
        for letter in word:
            child = curNode.children.get(letter)
            if not child:
                return False
            curNode = child
        
        # print("search:", word, str(curNode.isWord))
            
        return curNode.isWord
        
        
    def searchPrefix(self, prefix):
        if not prefix:
            return False
            
        curNode = self.root
        for letter in prefix:
            child = curNode.children.get(letter)
            if not child:
                return False
            curNode = child
            
        return True
'''