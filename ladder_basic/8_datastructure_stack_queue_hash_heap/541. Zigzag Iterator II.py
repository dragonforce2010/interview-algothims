'''
Follow up Zigzag Iterator: What if you are given k 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

Example
Given k = 3 1d vectors:

[1,2,3]
[4,5,6,7]
[8,9]
Return [1,4,8,2,5,9,3,6,7].
'''
# using dequeue and enqueue to implement the data zigzag iterator
class ZigzagIterator2:

    # @param {int[][]} a list of 1d vectors
    def __init__(self, vecs):
        # initialize your data structure here
        self.queue = [v for v in vecs if v] # this will remove all the empty v 


    def next(self):
        # Write your code here
        v = self.queue.pop(0)
        value = v.pop(0)
        if v:
            self.queue.append(v)
        return value


    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0
        

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
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

self.queue = [v for v in vecs if v]
'''