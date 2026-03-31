class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in points:
            d = (((i[0]*i[0])+(i[1]*i[1]))**0.5)
            heapq._heappush_max(res, (d, i))
            if len(res) > k:
                heapq._heappop_max(res)
        fres = [] 
        for i in res:
            fres.append(i[1])
        return fres

        