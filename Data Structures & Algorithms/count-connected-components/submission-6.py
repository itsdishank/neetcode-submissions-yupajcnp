class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in g[node]:
                dfs(nei)

        ct = 0
        for node in g:
            if node not in visit:
                dfs(node)
                ct += 1
        return ct + n - len(visit)