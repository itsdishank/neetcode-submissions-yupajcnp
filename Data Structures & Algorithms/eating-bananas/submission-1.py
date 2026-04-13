class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        ans = r
        
        def isValid(k):
            ct = 0
            for p in piles:
                ct += (p+k-1)//k
                # print(k, ct)
            return ct <= h

        while l <= r:
            mid = l+((r-l)//2)
            # print()
            if isValid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans