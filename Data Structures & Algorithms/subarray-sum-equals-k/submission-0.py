class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sumCt = {}
        cumSum = 0
        res = 0 
        for n in nums:
            cumSum += n
            if cumSum == k:
                res += 1
            diff = cumSum-k
            if diff in sumCt:
                res += sumCt[diff]
            sumCt[cumSum] = sumCt.get(cumSum, 0)+1
        
        return res