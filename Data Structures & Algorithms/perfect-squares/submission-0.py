class Solution:
    def numSquares(self, n: int) -> int:
        # dp = {}
        # def dfs(num):
        #     # if num == 0:
        #     #     return 0
        #     if not num:
        #         return num
        #     if num in dp:
        #         return dp[num]
        #     i = 1
        #     dp[num] = float('inf')
        #     while i**2 <= num:
        #         dp[num] = min(dp[num], 1 + dfs(num-(i**2)))
        #         i+=1
        #     return dp[num]
        
        # return dfs(n)

        dp = [10001]*(n+1)
        dp[0] = 0

        for num in range(1, n+1):
            i = 1
            while i**2 <= num:
                dp[num] = min(dp[num], 1 + dp[num-(i**2)])
                i+=1
        # print(dp)
        return dp[n]
        
                

        