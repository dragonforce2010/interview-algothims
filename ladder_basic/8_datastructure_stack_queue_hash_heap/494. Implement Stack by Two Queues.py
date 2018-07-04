'''
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Example
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
'''
class Stack:
    # initialize your data structure here.
    def __init__(self):
        import Queue # python2
        self.q1 = Queue.Queue()
        self.q2 = Queue.Queue()

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        self.q1.put(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        elem = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1    
        return elem

    # @return an integer, return the top of the stack
    def top(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
        ele = self.q1.get()
        self.q2.put(ele)
        self.q1, self.q2 = self.q2, self.q1
        return ele

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        return self.q1.empty()

'''
算法武器：queue

queue的特点是先进先出，我们可以维护元素的顺序，是的进入队列和出队列的顺序一致。

算法思路：

使用两个queue，queue1代表数据队列，我们把所有的元素都放到queue1中，queue2是辅助队列，用于元素临时中转操作
push操作，总是把元素放入到queue1中
pop操作，把queue1的元素逐一出队，逐一放入queue2中，唯独最后一个元素不放人，而是直接返回，然后交换queue1和queue2，这样就实现了pop
top操作，和pop操作很像，只是对于“最后一个元素不放入”，改为将最后一个元素放入到queue2中，然后交换queue1和queue2

'''