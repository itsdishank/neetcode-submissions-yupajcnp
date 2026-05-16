class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            ind = abs(n)-1
            if nums[ind] < 0:
                return ind+1
            nums[ind] *= -1