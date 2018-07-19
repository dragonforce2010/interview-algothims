'''
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
'''
class Solution:
    def __init__(self):
        self.father = []

    def numIslands2(self, n, m, operators):
        dirs = [
            (0, 1), 
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        islandCount, result = 0, []
        for i in range(n * m):
            self.father.append(-1)

        for point in operators:
            index = point.x * m + point.y
            if self.father[index] == -1:
                islandCount += 1
                self.father[index] = index
            else:
                result.append(islandCount)
                continue

            for dx, dy in dirs:
                x = point.x + dx
                y = point.y + dy

                if self.check(x, y, n, m):
                    if self.union(x * m + y, index):
                        if self.union(x * m + y, index):
                            islandCount -= 1

        def union(self, x, y):
            if self.father[x] == -1 or self.father[y] == -1:
                return False

            x = self.find(x)
            y = self.find(y)
            if x != y:
                self.father[x] = y
                return True
            else:
                return False

        def find(self, x):
            if self.father[x] == x:
                return x

            self.father[x] = self.find(self.father[x])
            return self.father[x]

        def check(self, x, y, n, m):
            return x >= 0 and y >= 0 and x < n and y < m