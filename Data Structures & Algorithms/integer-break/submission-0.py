class Solution:
    def integerBreak(self, n: int) -> int:
        d = {}
        d[2] = 1
        for i in range(3, n+1):
            d[i] = 1
            for j in range(2, i):
                d[i] = max(d[i], (i-j)*d[j], (i-j)*j)
        
        # print(d)
        return d[n]

        