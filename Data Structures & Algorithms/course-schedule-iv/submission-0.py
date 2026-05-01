class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)

        for s, d in prerequisites:
            g[s].append(d)
        
        # print(g)
        d = {}
        def dfs(node):
            if node in d:
                return d[node]
            res = set()
            for nei in g[node]:
                res = res | dfs(nei) | {nei}
            d[node] = res
            return res        


        for c in range(numCourses):
            dfs(c)

        ans = []
        for a, b in queries:
            if b in d[a]:
                ans.append(True)
            else:
                ans.append(False)
        return ans