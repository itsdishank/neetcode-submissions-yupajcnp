class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[float('inf')] * 2 for i in range(n)]
        print(dp)
        def dfs(i, buy):
            if i == n:
                return 0
            if dp[i][buy] != float('inf'):
                return dp[i][buy]
            
            res = dfs(i+1, buy)
            if buy:
                res = max(res, prices[i] + dfs(i+1, False))
            else:
                res = max(res, -prices[i] + dfs(i+1, True))
            dp[i][buy] = res
            return res

        return dfs(0, False)

        