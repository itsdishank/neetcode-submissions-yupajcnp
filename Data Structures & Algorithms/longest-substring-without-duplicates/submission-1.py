class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        res = 0
        for r, c in enumerate(s):
            if c in d:
                l = max(l, d[c]+1)
            d[c] = r
            res = max(res, r-l+1)

        return res