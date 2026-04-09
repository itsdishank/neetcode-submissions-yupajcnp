"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = 0
        t = []
        for i in intervals:
            t.append((i.start, 1))
            t.append((i.end, -1))
        
        t.sort()

        res = 0
        rooms = 0
        for time in t:
            rooms += time[1]
            res = max(res, rooms)
        
        return res