class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = 1

        pref = []
        for n in nums:
            pref.append(cur)
            cur *= n
        # print(pref)

        cur = 1

        for i in range(len(nums)-1, -1, -1):
            pref[i] *= cur
            cur *= nums[i]
        return pref