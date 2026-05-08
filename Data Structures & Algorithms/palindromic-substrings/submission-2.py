class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        l, r = 0, 0

        while l < n:
            while r < n and s[r] == s[l]:
                r += 1

            d = r - l
            res += (d+1)*d//2
            ll, rr = l-1, r
            while ll >= 0 and rr < n and s[ll] == s[rr]:
                ll -= 1
                rr += 1
                res += 1
            l = r
        
        return res