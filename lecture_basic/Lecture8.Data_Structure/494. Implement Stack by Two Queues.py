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
class Solution:
    def __init__(self):
        from collections import deque
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        ele = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ele

    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        ele = self.q1.popleft()
        self.q2.append(ele)
        self.q1, self.q2 = self.q2, self.q1
        return ele

    def isEmpty(self):
        return len(self.q1) > 0