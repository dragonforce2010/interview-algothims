'''Description
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''
class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False
            
        m, n = len(board), len(board[0])
        self.visited = set()
        self.dirs = [
            (0, 1), # up
            (1, 0), # right
            (0, -1),# down
            (-1, 0) # left
        ]
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    self.visited.add((i, j))
                    res = self.dfs(board, word, i, j)
                    if res:
                        return True
                    self.visited.remove((i, j))
                    
        return False
        
        
    def dfs(self, board, word, x, y):
        if not word:
            return True
            
        if board[x][y] != word[0]:
            return False
            
        if len(word) == 1:
            return True
            
        for dx, dy in self.dirs:
            nx = x + dx
            ny = y + dy
            if self.validate(board, word, nx, ny):
                self.visited.add((nx, ny))
                res = self.dfs(board, word[1:], nx, ny)
                if res:
                    return True
                self.visited.remove((nx, ny))
                
                
    def validate(self, board, word, x, y):
        m, n = len(board), len(board[0])
        if x >= 0 and x < m and y >= 0 and y < n and (x, y) not in self.visited:
            return True
            
        return False
'''Summary
算法武器：深度优先遍历

注意：
- 使用深度优先遍历的方式搜索路径的时候，一定要注意对路径的回溯
- 当我们将要以当前点开始进行深搜的时候，我们需要把当前点置为访问过的标记
- 当我们结束了以当前点其实的搜索，我们需要回溯，也就是把当前点标记为没有访问过，这样从其他路径过来的节点就能够访问当前点了
- 递归结束条件：
- 当单词为空时，可以成功返回
- 当board给定位置处的点和word首字母不同，则可以直接返回False
- 考虑极端情形，即单词是一个字符，那么我们就不能够对其周围四个方形进行搜索了，所以我们这时仅需要判断是否board位置处的字符和该单词相同，相同则返回True
'''