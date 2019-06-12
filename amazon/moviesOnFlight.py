'''
https://aonecode.com/amazon-online-assessment-questions

You are on a flight and wanna watch two movies during this flight. 
You are given int[] movie_duration which includes all the movie durations. 
You are also given the duration of the flight which is d in minutes. 
Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min). 
Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

e.g. 
Input
movie_duration: [90, 85, 75, 60, 120, 150, 125]
d: 250

Output from aonecode.com
[90, 125]
90min + 125min = 215 is the maximum number within 220 (250min - 30min)
'''
class Solution:
    def findLongestMoivePairs(self, movies, flightDuration):
        if not movies:
            return []

        movies.sort()
        left, right = 0, len(movies) - 1
        ans = []
        while left < right:
            duration = movies[left] + movies[right]
            if duration > flightDuration:
                right -= 1
            else:
                ans = [left, right]
                left += 1

        return ans