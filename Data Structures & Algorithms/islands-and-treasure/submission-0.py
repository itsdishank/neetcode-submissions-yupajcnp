class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, dist):
            # 1. Base Cases: Bounds check or Wall (-1)
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1:
                return
            
            # 2. Optimization: If the current cell already has a smaller (or equal) distance
            # than what we found, we stop. This prevents cycles and redundant work.
            if grid[r][c] < dist:
                return
            
            # 3. Update the cell with the new shortest distance
            grid[r][c] = dist
            
            # 4. Recurse to neighbors
            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        # 5. Start DFS ONLY from the Treasures (0)
        # We iterate to find where to START our push.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # Start DFS with distance 0
                    dfs(r, c, 0)