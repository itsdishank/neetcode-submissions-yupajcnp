class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if r == row - 1 and c == col-1:
                    continue
                elif r == row -1:
                    grid[r][c]+=grid[r][c+1]
                elif c == col -1:
                    grid[r][c]+=grid[r+1][c]
                else:
                    grid[r][c] += min(grid[r+1][c], grid[r][c+1])
        return grid[0][0]
        