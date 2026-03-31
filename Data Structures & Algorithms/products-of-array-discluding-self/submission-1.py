class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        prod = 1
        for n in nums:
            if n != 0:
                prod *= n
            else:
                zero_cnt +=1
        
        res = [0] * len(nums)
        if zero_cnt > 1:
            return res

        for i in range(len(nums)):
            if zero_cnt:
                res[i] = 0 if nums[i] else prod
            else:
                res[i] = prod//nums[i]
            
        return res


