class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        for a in t:
            if s[a] == 0:
                return a
            else:
                s[a] -= 1
        