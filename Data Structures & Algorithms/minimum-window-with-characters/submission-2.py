class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        windowCt = {}
        tCt = {}
        have = 0

        for c in t:
            tCt[c] = 1 + tCt.get(c, 0)

        need = len(tCt)
        resL = float('inf')
        res = (-1, 0)

        for r in range(len(s)):
            if s[r] in tCt:
                windowCt[s[r]] = 1 + windowCt.get(s[r], 0)
                if windowCt[s[r]] == tCt[s[r]]:
                    have += 1
            while have == need and l<=r:
                if r-l+1 < resL:
                    resL = r-l+1
                    res = (l,r)
                if s[l] in tCt:
                    windowCt[s[l]] -= 1
                    if windowCt[s[l]]+1 == tCt[s[l]]:
                        have -= 1
                l+=1
        
        return s[res[0]:res[1]+1] if resL != float('inf') else ""