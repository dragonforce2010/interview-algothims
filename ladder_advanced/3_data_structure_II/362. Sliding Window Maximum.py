'''Description
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.
'''
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            # each num has to be pushed into queue
            dq.append(i)
            
            # the below two ifs can make sure that we maintain a k size window
            if dq[0] == i - k:
                dq.popleft()
            # 开始收集答案
            if i >= k - 1:
                ans.append(nums[dq[0]])
        return ans
'''Summary
算法武器： 双端队列
使用双端队列维护窗口
将元素的下标放入到队列中
在队列中只保存最大元素，如果队中最右元素比当前元素小，则不断出队pop()，从右边移除
当队头元素的下标大于i - k, 即已经超出了窗口范围，我们需要将其移除，popleft()，这是从左边移除
当下标>= k - 1时，我们可以输出流式答案，左边即为答案，我们将其写入ans
遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标
由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)
记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]
若deque中的元素下标＜ i - (k - 1)，则将其从队头弹出，deque中的元素按照下标递增顺序从队尾入队。
这样就确保deque中的数组下标范围为[i - (k - 1), i]，满足滑动窗口的要求。
当下标i从队尾入队时，顺次弹出队列尾部不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）
deque的队头元素即为当前滑动窗口的最大值
'''