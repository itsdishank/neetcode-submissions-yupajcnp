import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i = 0
        n = len(queries)
        for j in range(len(queries)):
            queries[j] = (queries[j], j)
        queries.sort()
        intervals.sort()

        minH = []
        result = [-1] * n
        for q, ind in (queries):
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(minH, 
                               (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            while minH and minH[0][1] < q: heapq.heappop(minH)
            if minH: result[ind] = minH[0][0]
        return result