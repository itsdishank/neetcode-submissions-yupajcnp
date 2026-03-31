class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r):
            if r == n:
                ans[0] += 1
                return
            
            for c in range(n):
                if c in placedCol or r + c in placedPos or r - c in placedNeg:
                    continue

                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                backtrack(r + 1)

                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        placedCol = set() 
        placedPos = set() 
        placedNeg = set()  
        ans = [0]  

        backtrack(0)
        return ans[0]

        
        