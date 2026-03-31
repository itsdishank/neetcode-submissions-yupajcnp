class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevend = intervals[0][1]
        ct = 0

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s >= prevend:
                prevend = e
            else:
                ct += 1
                prevend = min(prevend, e)

        return ct