class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax = 0
        resMax = nums[0]
        curMin = 0
        resMin = nums[0]
        for n in nums:
            if curMax < 0:
                curMax = 0
            curMax += n
            resMax = max(curMax, resMax)
            if curMin > 0:
                curMin = 0
            curMin += n
            resMin = min(curMin, resMin)
        # print(sum(nums), resMax, resMin)

        s = sum(nums)

        if s == resMin:
            return resMax

        return max(resMax, sum(nums)-resMin)


        