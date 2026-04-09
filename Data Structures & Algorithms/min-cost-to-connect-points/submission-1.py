class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minH = [(0, 0)]
        visited = set()
        res = 0

        while minH or len(visited) < len(points):
            w, n = heapq.heappop(minH)
            x, y = points[n]
            if n in visited:
                continue
            visited.add(n)

            res += w

            for p in range(len(points)):
                if p not in visited:
                    neiX, neiY = points[p]  
                    heapq.heappush(minH, (abs(x - neiX) + abs(y - neiY) ,p))

        return res

