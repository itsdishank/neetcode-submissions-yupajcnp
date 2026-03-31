class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1 = r2 = 0

        for i in range(len(nums) - 1):
            cur = max(r2, nums[i]+r1)
            r1 = r2
            r2 = cur
        ans1 = r2
        r1 = r2 = 0
        for i in range(1, len(nums)):
            cur = max(r2, nums[i]+r1)
            r1 = r2
            r2 = cur
        ans2 = r2
        return max(ans2, ans1) 

        