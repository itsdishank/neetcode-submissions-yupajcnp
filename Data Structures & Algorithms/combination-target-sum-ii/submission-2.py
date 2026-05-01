class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        cur = []

        def dfs(i, curSum):
            if curSum == target:
                res.append(cur.copy())
                return
            if curSum >target or i == n:
                return

            cur.append(candidates[i])
            dfs(i+1, curSum + candidates[i])
            cur.pop()

            while i+1  < n and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i+1, curSum)

        dfs(0, 0)
        return res
