'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example
There exist two distinct solutions to the 4-queens puzzle:

[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
Challenge
Can you do it without recursion?
'''
class Solution:
    def solveNQueens(self, n):
        self.n = n
        # 保存皇后所在的行列
        self.colRowMap = {}
        self.results = []
        
        self.search(0)

        return self.results

    # 从当前行row开始搜索皇后可能的摆放位置，一直搜索到最后一行
    def search(self, row):
        # 当我们搜索完最后一行后，代表我们确实找到了一组解，我们把它打印出来
        if row == self.n:
            board = []
            for i in range(self.n):
                # 每一行我们先初始化为.......
                r = ['.'] * self.n
                # 因为每一行都肯定有皇后，我们从国colRowMap来查询皇后在当前行的列坐标，然后填充皇后字符
                r[self.colRowMap[i]] = 'Q'
                # 将改行的输出添加到board中
                board.append(''.join(r))
            self.results.append(board)
            return

        for col in range(self.n):
            if col in self.colRowMap:
                continue
            # 检测是否存在攻击情况
            if self.attack(row, col):
                continue
            
            # 标记皇后的位置
            self.colRowMap[col] = row
            # 递归搜索
            self.search(row + 1)
            # 回溯
            del self.colRowMap[col]

    def attack(self, row, col):
        for c, r in self.colRowMap.items():
            if abs(col - c) == abs(row - r):
                return True
        
        return False
