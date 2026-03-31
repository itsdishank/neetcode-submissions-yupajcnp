class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        # if nums[r] < target:
        #     return r+1

        while l<r:
            mid  = l + ((r-l)//2)
            print(l,mid,r)
            if nums[mid] >= target:
                r = mid
            else:
                l = mid+1

        # print(l,mid, r)
            
        return l
        