class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)
        print(g)
        visit = set()
        seen = set()
        
        res = []
        
        def dfs(node):
            # print(node)
            if node in visit:
                return False            
            if node in seen:
                return True

            visit.add(node)
            for nei in g[node]:
                if not dfs(nei):
                    return False
            res.append(node)
            visit.remove(node)
            seen.add(node)

            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
            # print()
        
        return res[::-1]