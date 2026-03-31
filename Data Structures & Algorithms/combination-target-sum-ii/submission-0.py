class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def dfs(i, tot):
            # print(curr)
            if tot == target:
                res.append(curr.copy())
                return
            if i == len(candidates) or tot > target:
                return

            curr.append(candidates[i])
            dfs(i+1, tot + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, tot)

        dfs(0, 0)
        return res