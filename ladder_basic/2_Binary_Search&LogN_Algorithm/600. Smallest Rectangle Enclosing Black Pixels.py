'''
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example
For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
'''
class Solution(object):
    # @param image {List[List[str]]}  a binary matrix with '0' and '1'
    # @param x, y {int} the location of one of the black pixels
    # @return an integer
    def minArea(self, image, x, y):
        # Write your code here
        if not image:
            return 0
        
        m, n = len(image), len(image[0])
        left = self.findLeftPos(m, n, y, image)
        right = self.findRightPos(m, n, y, image)
        up = self.findUpPos(m, n, x, image)
        down = self.findDownPos(m, n, x, image)
        
        return (right - left + 1) * (down - up + 1)
        
    def findRightPos(self, m, n, y, image):
        start, end = y, n - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if self.checkColumn(image, mid):
                start = mid
            else:
                end = mid - 1
        return start
    
    def findLeftPos(self, m, n, y, image):
        start, end = 0, y
        while start < end:
            mid = start + (end - start) / 2
            if self.checkColumn(image, mid):
                end = mid
            else:
                start = mid + 1
        return start
    
    def findDownPos(self, m, n, x, image):
        start, end = x, m - 1
        while start < end:
            mid = start + (end - start) / 2 + 1
            if self.checkRow(image, mid):
                start = mid
            else:
                end = mid - 1
        return start
    
    def findUpPos(self, m, n, x, image):
        start, end = 0, x
        while start < end:
            mid = start + (end - start) / 2
            if self.checkRow(image, mid):
                end = mid
            else:
                start = mid + 1
        return start
        

    # check if there are any black pixels in given column
    def checkColumn(self, image, col):
        rows = len(image)
        for i in xrange(rows):
            if image[i][col] == '1':
                return True
        return False

    # check if there are any black pixels in given row
    def checkRow(self, image, row):
        cols = len(image[0])
        for j in xrange(cols):
            if image[row][j] == '1':
                return True
        return False

'''
算法思想：二分法（上下左右进行四次二分法）

算法思路：

从左往右扫描找到第一个为黑点的位置

从左往右扫描找到最末个为黑点的位置

从上到下扫描找到第一个为黑点的位置

从上到下扫描找到最末个为黑点的位置

确定上下左右的边界之后，利用公式求解面积

area = (right - left + 1) * (down - up + 1)

注意：
二分法在一个算法题目中可以被使用多次，所以不要想当然认为一个算法中是使用1个二分
'''