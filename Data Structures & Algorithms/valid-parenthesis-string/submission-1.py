class Solution:
    def checkValidString(self, s: str) -> bool:
        o = st = c = 0

        for ch in s:
            if ch == '(':
                o += 1
            elif ch == ')':
                c += 1
            else:
                st += 1
            if o + st < c:
                return False

        o = st = c = 0
        for ch in reversed(s):
            if ch == '(':
                o += 1
            elif ch == ')':
                c += 1
            else:
                st += 1
            if c + st < o:
                return False
        
        return True
                

        