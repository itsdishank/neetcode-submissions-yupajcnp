class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        minH = []
        rows = len(grid)
        cols = len(grid[0])

        # def bfs(r,c):
        #     q = deque()


        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (min(nr, nc)>= 0 and nr < rows and nc < cols
                        and grid[nr][nc] == 2147483647):
                        grid[nr][nc] = dist
                        q.append((nr, nc))
            dist+=1
