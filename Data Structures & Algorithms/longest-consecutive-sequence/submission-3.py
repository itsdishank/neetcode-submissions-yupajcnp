class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            if n-1 not in s:
                i = 0
                ct = 0
                while n+i in s:
                    i+=1
                    ct += 1
                res = max(ct, res)
        
        return res