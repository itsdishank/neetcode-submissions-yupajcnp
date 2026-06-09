class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s//2
        dp = {}

        def dfs(i, total):
            if total == target:
                return True
            if total > target:
                return False
            if i == len(nums):
                return False
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i+1, total) or dfs(i+1, total + nums[i])

            return dp[(i, total)]

        return dfs(0, 0)