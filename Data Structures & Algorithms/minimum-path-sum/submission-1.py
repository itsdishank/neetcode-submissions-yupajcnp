class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [float('inf')]*(cols)
        dp[-1] = 0 

        for r in range(rows-1, -1, -1):
            new_dp = [float('inf')]*(cols+1)
            for c in range(cols-1, -1, -1):
                new_dp[c] = grid[r][c] + min(dp[c], new_dp[c+1])
            dp = new_dp
            # print(dp)

        # print(dp)
        return dp[0]