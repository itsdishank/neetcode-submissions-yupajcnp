class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minn = prices[0]

        for i in range(1, len(prices)):
            minn = min(minn, prices[i])
            res = max(res, prices[i]-minn)

        return res