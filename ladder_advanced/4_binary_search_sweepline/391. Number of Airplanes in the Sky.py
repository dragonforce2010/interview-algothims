'''Description
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

Notice
If landing and flying happens at the same time, we consider landing should happen at first.
Example
For interval list

[
  (1,10),
  (2,3),
  (5,8),
  (4,7)
]
Return 3
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# airplanex data structure: (airplance.start/airplance.end, delta)
# sort by time first
# if time is same, then sort by delta value
# detla = 1, if the airplance is taking off
# detla = -1, if the airplance is landing
def sorter(airplanex, airplaney):
    if airplanex[0] != airplaney[0]:
        return airplanex[0] - airplaney[0]
    return airplanex[1] - airplaney[1]


class Solution:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # elements in timepoints array is a tuple (airplance.start, delta)
        # detla = 1, if the airplance is taking off
        # detla = -1, if the airplance is landing
        timepoints = []
        for airplane in airplanes:
            timepoints.append((airplane.start, 1))
            timepoints.append((airplane.end, -1))
            
        timepoints = sorted(timepoints, cmp=sorter)
        
        # sum: the count of airplane in the sky
        # mostï¼ the largest sum
        sum, most = 0, 0
        # sweep line
        for t, delta in timepoints:
            sum += delta
            most = max(most, sum)
            
        return most
'''Summary
'''