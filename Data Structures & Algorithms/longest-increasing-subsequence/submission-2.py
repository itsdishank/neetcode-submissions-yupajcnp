class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp  = [1] * len(nums)
        res = 0

        for i in range(len(nums)-1, -1, -1):
            cur_max = 0
            for j in range(i+1, len(nums)):
                if nums[j] >nums[i]:
                    cur_max = max(cur_max, dp[j])
            dp[i] = cur_max+1
            res = max(dp[i], res)
            # print(dp)
        return res
        