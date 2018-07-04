'''
There are two properties in the node student id and scores, to ensure that each student will have at least 5 points, find the average of 5 highest scores for each person.

Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return 
'''
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
import heapq
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        # Write your code here
        hash = dict()
        for r in results:
            if r.id not in hash:
                hash[r.id] = []
            
            heapq.heappush(hash[r.id], r.score)
            if len(hash[r.id]) > 5:
                heapq.heappop(hash[r.id])

        # answer = dict()
        for id, scores in hash.items():
            hash[id] = sum(scores) / 5.0

        return hash
'''
算法武器：hash + heap

本题考查哈希表的使用方法
哈希表键值为id，值为成绩数组
最后遍历这个哈希表，利用成绩数组，计算成绩均值

学会遍历哈希表的键值队，使用hash.items()这个函数
'''