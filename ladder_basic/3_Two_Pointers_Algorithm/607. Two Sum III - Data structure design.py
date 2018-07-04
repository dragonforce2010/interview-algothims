'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''
class TwoSum(object):
    
    def __init__(self):
        # initialize your data structure here
        self.count = {}
        

    # Add the number to an internal data structure.
    # @param number {int}
    # @return nothing
    def add(self, number):
        # Write your code here
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

        

    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        # Write your code here
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False
        # Write your code here
        


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
'''
算法武器：双指针 + 哈希表

本题和lintcode 56题的two sum 需要比较一下，本题的hash的value存储了元素的数量。因为本题的hash变量是类成员变量，我们每次在进行find查找的时候不重新构建hash，而是使用成员变量，那么这时候我们需要处理一个比较tricky的问题，就是当一个数的补数（value - num）就是其自身的时候并且已存在在hash表中，我们还不能够轻易断定当前数组中就存在twosum = value，我们还需要从元素数量上进行判定，如果hash中的该元素的数量是大于1，那么我们才返回true。

如果我们每次进行find查找时都重建hash，那么我们就不需要保存元素数量了。
'''