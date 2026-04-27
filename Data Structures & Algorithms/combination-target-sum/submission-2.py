class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        def dfs(i, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum > target or i == n:
                return

            # skip
            dfs(i+1, curSum)
            # take
            # for j in range(i, n):
            cur.append(nums[i])
            dfs(i, curSum + nums[i])
            cur.pop()
            return 
        
        dfs(0, 0)
        return res


            