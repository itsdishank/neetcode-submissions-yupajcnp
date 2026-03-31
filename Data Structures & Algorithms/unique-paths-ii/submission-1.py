class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        col = len(obstacleGrid[0])
        row = len(obstacleGrid)   

        dp = [0] * (col+1)
        dp[-2] = 1
        for r in range(row-1, -1, -1):
            for c in range(col-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] += dp[c+1]
        return dp[0]