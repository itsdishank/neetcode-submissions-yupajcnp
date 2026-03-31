class Solution:
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1

        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return c
        i = 3
        while i<=n:
            new = a+b+c
            a = b
            b = c
            c = new
            i+=1
        return c
             
        