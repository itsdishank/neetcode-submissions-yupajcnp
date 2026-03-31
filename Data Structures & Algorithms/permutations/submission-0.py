class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        
        def dfs(s, l):
            for i in range(len(nums)):
                if len(s) == len(nums):
                    res.append(l.copy())
                    return
                if i not in s:
                    s.add(i)
                    l.append(nums[i])
                    dfs(s, l)
                    s.remove(i)
                    l.pop()

        dfs(set(),[])
        return (res)