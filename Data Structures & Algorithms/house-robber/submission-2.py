class Solution:
    def rob(self, nums: List[int]) -> int: 
        r1, r2 = 0, 0
        
        for n in range(len(nums)):
            cur = max(nums[n]+r1, r2)
            r1 = r2
            r2 = cur
        
        return r2