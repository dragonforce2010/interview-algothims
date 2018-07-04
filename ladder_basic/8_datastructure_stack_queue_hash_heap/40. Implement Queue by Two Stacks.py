'''
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.

Example
push(1)
pop()     // return 1
push(2)
push(3)
top()     // return 2
pop()     // return 2
Challenge
implement it by two stacks, do not use any other data structure and push, pop and top should be O(1) by AVERAGE.
'''
class MyQueue:
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
                
    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.adjust()
        return self.stack2[len(self.stack2) - 1]

    def pop(self):
        self.adjust()
        return self.stack2.pop()

'''
算法武器：栈

算法思路：

使用stack1作为数据栈，保存入栈元素，即push操作全部push到stack1中
使用stack2作为数据栈，用于出栈元素，即pop元素都从stack2中pop出来
但是注意，从stack2中pop数据时，我们要做一个判断：
如果stack2为空，那么我们需要把数据从stack1出栈到stack2中，这样stack1中的数据就可以像队列一样的顺序输出了，因为数据的顺序经过栈的翻转改变了。
如果stack2不为空，那么就持续从stack2中pop就好，如果有数据push进来，我们依然持续往statck1中push
adjust操作仅发生在stack2中的数据没了，消费完了，我们才从stack1中全部导入一次
'''