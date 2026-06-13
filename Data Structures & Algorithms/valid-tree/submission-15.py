class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visit = set()
        def dfs(node, parent):
            # print(node, parent, cycle)
            if node in visit:
                return False
            visit.add(node)
            
            for nei in graph[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True

        res = dfs(0, None)
        if len(visit) != n:
            return False
        return res