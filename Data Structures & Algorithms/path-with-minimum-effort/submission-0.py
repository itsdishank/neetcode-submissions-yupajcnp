class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visit = set()
        minH = [(0, 0, 0)]

        while minH:
            curEff, r, c = heapq.heappop(minH)

            if r == rows-1 and c == cols-1:
                return curEff

            if (r, c) in visit:
                continue
            
            visit.add((r, c))

            for dr, dc in dirs:
                nr = r+dr
                nc = c + dc
                if (
                    min(nr, nc)<0 or nc == cols
                    or nr == rows or (nr, nc) in visit
                ):
                    continue

                newEff = max(curEff, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(minH, (newEff, nr, nc))
            
        return 0
