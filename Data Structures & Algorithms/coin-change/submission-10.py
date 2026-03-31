class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [-1] * (amount + 1)
        dp[0] = 0

        def dfs(rem):
            if rem == 0:
                return 0
            if dp[rem] != -1:
                return dp[rem]

            res = amount + 1 
            for c in coins:
                if c <= rem:
                    res = min(res, dfs(rem - c))

            dp[rem] = res + 1
            return dp[rem]

        ans = dfs(amount)
        return -1 if ans > amount else ans