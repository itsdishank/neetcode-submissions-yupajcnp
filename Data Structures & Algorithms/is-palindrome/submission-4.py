class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        r = n-1
        l = 0
        while l<=r:
            while l < n and not s[l].isalnum():
                l += 1
            
            while r>= 0 and not s[r].isalnum():
                r -= 1
            
            # print(l, r, s[l], s[r])
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1

        return True

        