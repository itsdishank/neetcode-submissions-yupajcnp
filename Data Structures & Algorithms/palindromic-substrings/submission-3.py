class Solution:
    def countSubstrings(self, s: str) -> int:
        r = 0
        n = len(s)

        res = 0
        for r in range(n):
            nl, nr = r, r
            while nl >= 0 and nr < n and s[nl] == s[nr]:
                res += 1
                nl -= 1
                nr += 1
            
            nl, nr = r, r+1
            while nl >= 0 and nr < n:
                if s[nl] == s[nr]:
                    res += 1
                else:
                    break
                nl -= 1
                nr += 1
        return res
            

        