class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        nums = [1] + nums + [1]
        def burst(l, r):
            if r < l:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            if l == r:
                return nums[l] * nums[l-1] * nums[r+1]
            dp[(l, r)] = 0
            for i in range(l, r+1):
                left = burst(l, i-1)
                right = burst(i+1, r)
                dp[(l, r)] = max(dp[(l, r)], nums[i] * nums[l-1] * nums[r+1] + left + right)
            return dp[(l, r)]
        
        return burst(1, len(nums)-2)

        1, 1, 2, 3, 4, 5, 6, 7, 1
        0, 1, 2, 3, 4, 5, 6
        # burst(0, 6, 1, 1)
        # cur = 4 * 1 * 1  
        # burst(0, 2, 1, 4)                           burst(4, 6, 4, 1)
        # left = 1
        # right = 4
        # 2 * 1 * 4 +
        # burst(0, 0, 1, 2)        burst(2, 2, 2, 1)





    
