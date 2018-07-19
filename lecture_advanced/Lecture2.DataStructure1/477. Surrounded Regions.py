'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

Example
X X X X
X O O X
X X O X
X O X X
After capture all regions surrounded by 'X', the board should be:

X X X X
X X X X
X X X X
X O X X
'''
class Solution:
    # @param {list[list[str]]} board a 2D board containing 'X' and 'O'
    # @return nothing 
    def surroundedRegions(self, board):
        if not board:
            return board
            
        m, n = len(board), len(board[0])
        visited = set()
                
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0, visited)
            if board[i][n - 1] == 'O':
                self.dfs(board, i, n - 1, visited)
            
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j, visited)
            if board[m - 1][j] == 'O':
                self.dfs(board, m - 1, j, visited)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == '$':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                    
        return board
        
        
    def dfs(self, board, x, y, visited):
        m, n = len(board), len(board[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0,-1,  0]
        visited.add((x,y))
        board[x][y] = '$'
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= 0 and nx < m and ny >= 0 and ny < n and board[nx][ny] == 'O' and (nx, ny) not in visited:
                self.dfs(board, nx, ny, visited)
'''
算法武器：深度优先搜索 + 反向思考（找非解点）
本题需要使用反面思考的方式。
因为边缘部分的节点不能算作包围区域，与其我们想尽办法搜索包围区域中符合条件的点，在board内同时又不属于边缘，还不如我们把不符合条件的边缘的O找出来，我们把这些O标记为一个新的记号，那么剩下的O就是可以被填充的区域，这样从反面思考问题就简单了很多。

本题使用深度优先搜索又学习到了一个新的技巧：使用标记符号填充非目标区域，这样区分出目标和非目标之后，我们就能轻松填充目标区域了。

本题还是用了set的方式表示访问数组，注意我们只能把坐标元祖add到访问set中，list是不可以的。

在dfs函数内，我们总是标记该点被访问过，已经做相应业务处理，比如标记置位等。这些事情只在dfs内部做，我们不要把他放在外面，这样可以保持良好的封装性。

http://www.cnblogs.com/grandyang/p/4555831.html
这道题有点像围棋，将包住的O都变成X，但不同的是边缘的O不算被包围，跟之前那道Number of Islands 岛屿的数量很类似，都可以用DFS来解。刚开始我的思路是DFS遍历中间的O，如果没有到达边缘，都变成X，如果到达了边缘，将之前变成X的再变回来。但是这样做非常的不方便，在网上看到大家普遍的做法是扫面矩阵的四条边，如果有O，则用DFS遍历，将所有连着的O都变成另一个字符，比如，这样剩下的O都是被包围的，然后将这些O变成X，把，这样剩下的O都是被包围的，然后将这些O变成X，把变回O就行了
'''