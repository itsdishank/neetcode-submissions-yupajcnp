class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curr):
            # print(curr)
            if i == len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i+1, curr)
            del curr[-1]
            dfs(i+1, curr)

        dfs(0, [])
        return res