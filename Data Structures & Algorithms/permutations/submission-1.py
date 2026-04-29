class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        visit = set()
        n = len(nums)
        def dfs(i):
            if i == n:
                # print(i, visit, cur)
                # print()
                res.append(cur.copy())
                return
            
            # visit.add
            for j in range(n):
                # print(i, j, visit, cur)
                if j not in visit:
                    visit.add(j)
                    cur.append(nums[j])
                    dfs(i+1)
                    cur.pop()
                    visit.remove(j)
            
        dfs(0)
        return res