class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            ind = abs(n)-1
            # print(ind)
            if nums[ind] < 0:
                return abs(n)
            nums[ind] *= -1
            # print(nums)