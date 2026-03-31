class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1
        l, r = 0, len(nums)-1
        if not nums:
            return [start, end]

        while l<r:
            mid = l+((r-l)//2)
            if nums[mid]< target:
                l = mid+1
            elif nums[mid]>= target:
                r = mid
        if nums[l] != target:
            return [start, end]
        start = l
        l, r = 0, len(nums)-1
        while l<r:
            mid = l+(math.ceil((r-l)/2))
            if nums[mid]<=target:
                l = mid
            elif nums[mid]>target:
                r = mid-1
        end = r
        return [start, end]
        