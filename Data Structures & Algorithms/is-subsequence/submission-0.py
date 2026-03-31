class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        
        if s == '': return True
        if len(s) > len(t): return False

        while j <len(t) and i < len(s):
            if s[i] == t[j]:
                i+=1
            j+=1

        if i == len(s):
            return True
        return False
