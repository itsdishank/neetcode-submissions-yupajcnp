class Solution:
    def rob(self, nums: List[int]) -> int:
        m = {}
        def dfs(n, d):
            if n >= len(nums):
                return 0
            key = (n,d)
            if key in m:
                return m[key]
            skip = dfs(n+1, False)
            take = 0
            if not d:
                take = nums[n] + dfs(n+1, True)
            
            m[key] = max(take,skip)
            return m[key]
            
        return dfs(0, False)