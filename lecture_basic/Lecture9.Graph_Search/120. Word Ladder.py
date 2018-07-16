'''
Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''
class Solution:
    def ladderLength2(self, start, end, dict):
        dict.add(end)
        wordLen = len(start)
        queue = collections.deque([(start, 1)])

        while queue:
            curWord, pathLen = queue.popleft()
            if curWord == end:
                return pathLen

            for i in range(wordLen):
                part1 = curWord[:i]
                part2 = curWord[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if curWord[i] != j:
                        nextWord = part1 + j + part2
                        if nextWord in dict:
                            queue.append((nextWord, pathLen + 1))
                            dict.remove(nextWord)

        return 0