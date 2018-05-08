'''Description
Implement an iterator to flatten a 2d vector.
Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].
'''
class Vector2D(object):
    
    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.vec2d = 0, -1, vec2d
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        # self.col += 1
        return self.vec2d[self.row][self.col]
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        self.col += 1
        while self.row < len(self.vec2d) and \
            self.col >= len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)
'''Summary
算法武器： 数组 + 基础编程能力
hasNext: 不仅检查是否还有下一个元素，同时移动row和col，使之指向下一个元素的位置。
数据矩阵中可能有很多空行，hasNext需要把这些空行都跳过，让row和col指向下一个元素的位置
注意：client在调用next时总是首先调用hasNext方法

本题难点：
- iterator重点在于控制游标，对于二维情况就是指row，col
- hasNext方法不仅检测是否有下一个元素，同时移动游标指向下一个元素
- 考虑到边界条件：一个数据矩阵中的行数据可能是空的，并且可能存在多个空行，那么在移动游标时就需要跳过这些空行
'''