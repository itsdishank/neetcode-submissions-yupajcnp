class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0, 0
        for n in nums:
            t = max(n+ h1, h2)
            h1 = h2
            h2 = t
        return h2
        