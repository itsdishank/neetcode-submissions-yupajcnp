class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0
        countT = defaultdict(int)
        for c in t:
            countT[c] +=1
        need = len(countT)
        minL = float('inf')
        minRes = ''

        l = 0
        countS = defaultdict(int)
        for r in range(len(s)):
            if s[r] in countT:
                countS[s[r]] += 1
                if countS[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if r-l+1 < minL:
                    minL = r-l+1
                    minRes = s[l:r+1]
                if s[l] in countT:
                    countS[s[l]] -=1
                    if countS[s[l]] + 1 == countT[s[l]]:
                        have -= 1
                l+=1

        return minRes

