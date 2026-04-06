class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, v in enumerate(nums):
            diff = target-v
            if diff in d:
                return [d[diff], i]
            else:
                d[v] = i
        