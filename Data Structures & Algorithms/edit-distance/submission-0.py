class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [len(word1) - i for i in range(len(word1) + 1)]


        for i in range(len(word2)-1, -1, -1):
            prev = dp[-1]
            dp[-1] += 1
            for j in range(len(word1)-1, -1, -1):
                # print(j, dp[j])
                res = dp[j]
                if word1[j] == word2[i]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j+1], dp[j], prev)
                prev = res
        return dp[0]

