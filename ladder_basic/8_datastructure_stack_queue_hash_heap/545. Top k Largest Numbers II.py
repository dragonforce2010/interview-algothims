'''
Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
Example
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
'''
import heapq

class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)
        
    # @param {int} num an integer
    def add(self, num):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num)
        elif num > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, num)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        return sorted(self.nums, reverse=True)
'''
算法武器：固定size的heap

求前k大/小的问题都要用到堆，同时本题还限定堆的尺寸，不能超过k。
求top k大的数，那么我们就维护一个最小堆，这样堆满的情况下，我们总是可以淘汰对顶元素，因为它是最小的，然后加入新的元素（前提：这个加入的元素比对顶元素大，这样我们才会淘汰堆顶）
'''