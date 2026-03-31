class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_ind = {}
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in char_ind:
                start = max(start, char_ind[s[i]]+1)
            char_ind[s[i]] = i
            # print(i, start, char_ind, res)
            res = max(res, i-start+1)

        return res
        