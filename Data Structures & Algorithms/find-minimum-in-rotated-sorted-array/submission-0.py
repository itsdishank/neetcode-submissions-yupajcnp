class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1  # min is in right half
            else:
                right = mid  # min is in left half (including mid)

        return nums[left]  # left == right is the index of the min element
