class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n+1)
        dp[-1] = 0   

        for i in range(n - 1, -1, -1):
            cur = 0
            for j in range(min(3, n-i)):
                cur += stoneValue[i+j]
                dp[i] = max(dp[i], cur - dp[i+j+1])
        #         print(j, cur, cur - dp[i+j+1])
        #     print()
        # print(dp)

        if dp[0]>0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
