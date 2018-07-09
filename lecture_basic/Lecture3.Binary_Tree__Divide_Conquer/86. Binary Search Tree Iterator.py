'''
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Example
For the following binary search tree, in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
'''
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curt = root

    # 当curt所指向的待处理子树不为空或者stack不为空，那么我们就可以继续输出下一个中序元素
    def hasNext(self):
        return self.curt or self.stack

    # 对于curt指向的子树，如果子树存在（cur指针不为空），那么我们就进入for循环，一直扫描到子树的最左节点
    def next(self):
        while self.curt:
            self.stack.append(self.curt)
            self.curt = self.curt.left

        # 不论while循环部分执行也好（curt不为空），或是不执行，我们下一个访问的元素一定保存在栈顶，所以要出栈
        node = self.stack.pop()
        # 更新self.curt指针，指向下一个待处理子树
        self.curt = node.right

        return node