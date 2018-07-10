'''
Given k sorted integer arrays, merge them into one sorted array.

Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.
'''
import heapq
class Solution:
    def mergeSortedArrays(self, arry):
        result, heap = []
        for row, array in enumerate(arrays):
            if array:
                heapq.heappush(heap, (array[0], row, 0))

        while heap:
            val, row, col = heapq.heappop(heap)
            result.append(val)
            if col + 1 < len(arrays[row]):
                heapq.heappush(heap, (arrays[row][col + 1], row, col + 1))

        return sesult
'''
算法武器： heap

这道题和把k个有序链表合并的思路一样的。都是使用heap，将每个数组的首元素加入heap，然后每次从heap中弹出的元素，
装入堆的是一个三元组：（元素值，元素在arrays中所在的row， 元素在arrays.col）
元组第一个分量用于堆排序依据和结果输出，第二个、第三个元素分量用于寻找下一个进入堆的元素的位置。
每次将元素入堆的时候都要判断元素是否在数组中存在。
'''