'''
Given two 1d vectors, implement an iterator to return their elements alternately.

Example
Given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
'''
class ZigzagIterator:
    
    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        self.queue = [v for v in (v1, v2) if v]
        # self.stack = [v1, v2]

    def next(self):
        v = self.queue.pop(0)
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value


    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

'''
算法武器： stack

本题有交替输出的需求，交替是改变输出顺序，对于顺序有影响的数据结构我们可以想到栈stack或者queue. 本题使用queue来进行求解。

我们可以想象list v1和v2在同一队列中，然后分别出队输出一个元素，再把自己（v1或者v2）放入队中，这样就实现了交替。

因为我们是用python的list []来模拟queue，所以我们使用了以下api，对于list v

v.pop(0)表示出队，发生在list的首部
v.append(item)表示元素入队，发生在list的尾部
注意初始化部分，我们不想让空list也加入队中，所以我们做了条件限制

self.queue = [v for v in (v1, v2) if v]
'''