class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            i = 1
            if n - 1 in nums:
                continue
            while n + i in nums:
                i+= 1
            res = max(i, res)
        return res
        