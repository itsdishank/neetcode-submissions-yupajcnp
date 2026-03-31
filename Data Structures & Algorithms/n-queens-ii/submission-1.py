class Solution:
    def totalNQueens(self, n: int) -> int:
        diag = set()
        negDiag = set()
        cols = set()
        res = 0

        def backtrack(r, c):
            if (min(r,c) < 0 or c == n or c in cols
                or r-c in diag or r+c in negDiag):
                return
            
            nonlocal res
            if r == n-1:
                res += 1
                return

            cols.add(c)
            diag.add(r-c)
            negDiag.add(r+c)

            for i in range(n):
                backtrack(r+1,i)

            cols.remove(c)
            diag.remove(r-c)
            negDiag.remove(r+c)

            return 

        for i in range(n):
            backtrack(0,i)


        return res
        