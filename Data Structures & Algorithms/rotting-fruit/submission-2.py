class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        ct = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ct += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = ((1, 0), (0, 1), (0, -1), (-1, 0))
        minute = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if min(nr, nc) >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        ct -= 1
            minute +=1
            # print(q)

        # print(ct, minute)
        if ct:
            return -1
        return  max(0, minute-1)

                 