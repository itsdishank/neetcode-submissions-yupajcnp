class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for c, p in prerequisites:
            g[c].append(p)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if not g[crs]:
                return True

            visit.add(crs)

            for c in g[crs]:
                if not dfs(c):
                    return False
            
            visit.remove(crs)
            g[crs] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        