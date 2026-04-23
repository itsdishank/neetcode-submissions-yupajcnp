class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[-1] = 0 

        for i in range(n-1, -1, -1):
            for w in dictionary:
                if len(w) > (n-i) or w != s[i:i+len(w)]:
                    continue
                dp[i] = min(dp[i], dp[i+len(w)])
            dp[i] = min(dp[i], 1+dp[i+1])
        return dp[0]