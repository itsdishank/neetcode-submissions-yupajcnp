class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)
        def dfs(i, state):
            if i >= n:
                return 0 
            if (i, state) in dp:
                return dp[(i, state)]

            # Hold
            hold = dfs(i+1, state)

            if state == 0:
                buy = dfs(i+1, 1) - prices[i]
                dp[(i, state)] = max(buy, hold)
            else:
                sell = dfs(i+2, 0) + prices[i]
                dp[(i, state)] = max(sell, hold)
            return dp[(i, state)]

        return dfs(0, 0)
