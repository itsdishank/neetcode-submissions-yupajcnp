class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for s, d in prerequisites:
            g[s].append(d)

        def dfs(node):
            if not g[node]:
                return True
            if node in visit:
                return False
            visit.add(node)
            
            for nei in g[node]:
                if not dfs(nei):
                    return False

            visit.remove(node)
            g[node] = []
            
            return True

        visit = set()
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True