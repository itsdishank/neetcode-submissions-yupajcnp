class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        res = 100001
        for r in range(len(nums)):
            s += nums[r]
            if s >= target:
                # res = min(r-l+1, res)
                while l<=r and s>= target:
                    res = min(r-l+1, res)
                    # print(res, l, r, s)
                    s -= nums[l]
                    l+=1
            # print(s)
            # print(l, r)
            # print(res)
            # print()
        return 0 if res == 100001 else res

        