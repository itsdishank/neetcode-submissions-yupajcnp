class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1

            if (i+1 < len(s) and int(s[i]+s[i+1]) in range(10,27)):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
        