class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        cycle  = set()
        visit = set()
        def dfs(node, parent):
            # print(node, parent, cycle)
            if node == None:
                return True
            if node in cycle:
                return False
            visit.add(node)
            cycle.add(node)
            
            for nei in graph[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False

            cycle.remove(node)
            
            return True
        res = dfs(0, None)
        if len(visit) != n:
            return False
        return res
        for i in range(n):
            if not dfs(0, None):
                return 