'''
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
'''
class MovingAverage(object):
    
    def __init__(self, size):
        # Initialize your data structure here.
        from Queue import Queue
        self.queue = Queue()
        # window size
        self.size = size
        # maintain window sum
        self.sum = 0.0
        

    # @param {int} val an teger
    def next(self, val):
        # Write your code here
        self.sum += val
        if self.queue.qsize() == self.size:
            self.sum -= self.queue.get()
        self.queue.put(val)
        return self.sum * 1.0 / self.queue.qsize()
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

'''
求滑动平均问题不难，使用window sum的方式很容求解。

对比求滑动最大值、最小值，相对来说就复杂多了，因为我们需要维持两个堆（一个最大堆和最小堆）
'''