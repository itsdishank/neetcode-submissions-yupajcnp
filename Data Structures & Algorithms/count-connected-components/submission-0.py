class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjL = defaultdict(list)
        for i, j in edges:
            adjL[i].append(j)
            adjL[j].append(i)
        print(adjL)
        v = set()
        def dfs(node, prev):
            if node in v:
                return 
            v.add(node)
            for n in adjL[node]:
                if n == [prev]:
                    continue
                dfs(n, node)
        
        count = 0
        for i in range(n):
            if i not in v:
                count += 1
                dfs(i, -1)
        # dfs(0, -1)
        print(v)
        print(count)

        return count
        
        