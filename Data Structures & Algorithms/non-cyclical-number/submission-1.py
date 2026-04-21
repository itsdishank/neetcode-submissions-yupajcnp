class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            newN = 0
            for i in str(n):
                newN += int(i)**2
            n = newN
            if n in s:
                return False
            s.add(n)
        return True
        