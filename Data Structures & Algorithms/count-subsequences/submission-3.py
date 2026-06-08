class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # res[0] = 0
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = 1
        for row in dp:
            row[-1] = 1

        rows = len(s)
        cols = len(t)

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                dp[r][c] += dp[r+1][c]
                if s[r] == t[c]:
                    dp[r][c] += dp[r+1][c+1]
        return dp[0][0]
                