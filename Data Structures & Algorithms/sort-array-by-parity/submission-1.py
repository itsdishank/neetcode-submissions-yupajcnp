class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        i = 0
        while i <= r:
            if nums[i]%2:
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            else:
                nums[i], nums[l] = nums[l], nums[i]
                l+=1
                i+=1
        return nums
            
        