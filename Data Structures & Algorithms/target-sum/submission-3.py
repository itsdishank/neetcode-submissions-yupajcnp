class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        if abs(target) > tot:
            return 0
        s = tot*2+1
        dp = [0] * (s)
        # print(dp)
        dp[tot] = 1

        for n in nums:
            newDP = [0] * (s)
            for i in range(s):
                if dp[i] != 0:
                    newDP[i-n] += dp[i]
                    newDP[i+n] += dp[i]
            dp = newDP
            # print(dp)
        return dp[tot+target]