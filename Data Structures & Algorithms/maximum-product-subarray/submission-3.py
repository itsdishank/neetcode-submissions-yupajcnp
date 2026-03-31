class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax = curMin = 1

        for i in nums:
            if i == 0:
                curMin = curMax = 1
                continue
            
            temp = curMax
            curMax = max(curMax*i, curMin*i, i)
            curMin = min(temp*i, curMin*i, i)
            res = max(curMax, res)

        return res
        