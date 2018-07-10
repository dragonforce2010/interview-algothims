'''
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.

Example
push(1)
pop()   // return 1
push(2)
push(3)
min()   // return 2
push(1)
min()   // return 1
'''
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, number):
        self.stack.append(number)
        if not self.minstack or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()

        return self.stack.pop()

    def min(self):
        return self.minstack[-1]
'''
算法武器：最小栈

最小栈的使用方法：

当数据进入数据栈时，判断最小栈是否有元素或是进入的数据比最小栈的栈顶数据还小，那么就将该数据也推入最小栈
当进入数据等于最小栈栈顶数据时，我们也将该数据推入最新哦啊哦栈
当数据出栈时，我们判断出栈的数据是否等于最小栈栈顶的数据，如果相等，则最小栈也需要出栈一个元素
当查看当前栈中的最小数据时，我们返回最小栈的栈顶数据即可
'''