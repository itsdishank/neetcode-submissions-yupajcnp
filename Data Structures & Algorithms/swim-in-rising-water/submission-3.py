class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minH = [(grid[0][0], 0, 0)]
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        while minH:
            val, r, c = heapq.heappop(minH)
            res = max(res, val)
            if r == rows-1 and c == cols-1:
                return res
            if (r, c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in directions:
                nr = r+dr
                nc = c+dc
                if min(nr, nc) >= 0 and nr < rows and nc < cols and (nr, nc) not in visit:
                    heapq.heappush(minH, (grid[nr][nc], nr, nc))
            # print(minH)
        return -1











