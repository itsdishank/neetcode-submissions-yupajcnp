class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0     
        res = resL = resR = 0   
        while i < len(s):
            l = r = i
            while r+1 < len(s) and s[r+1] == s[r]:
                r += 1
            
            while l>=0 and r < len(s) and s[l] == s[r]:
                curRes = r-l+1
                if curRes > res:
                    resL = l
                    resR = r
                    res = curRes

                # res = max(r-l+1, res)
                l-=1
                r+=1
            i+= 1

        return s[resL:resR+1]