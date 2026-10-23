class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset *= 2
            res.append(res[i-offset]+1)
        return res
            
