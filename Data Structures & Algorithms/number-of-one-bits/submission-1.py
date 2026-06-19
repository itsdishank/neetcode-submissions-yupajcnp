class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0
        while n:
            if 1&n:
                ct +=1
            n >>= 1

        return ct