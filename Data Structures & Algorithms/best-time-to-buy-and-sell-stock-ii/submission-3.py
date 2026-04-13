class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * 2
        print(dp)
        
        
        for i in range(n - 1, -1, -1):
            next_dp = [0, 0]
            next_dp[0] = max(dp[0], -prices[i] + dp[1]) 
            next_dp[1] = max(dp[1], prices[i] + dp[0]) 
            dp = next_dp
        
        return dp[0]


        