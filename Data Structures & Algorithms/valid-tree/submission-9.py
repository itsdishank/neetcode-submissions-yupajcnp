class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL =  defaultdict(list)
        for i, j in edges:
            adjL[i].append(j)
            adjL[j].append(i)

        visitSet = set() 
        print(adjL)

        def dfs(prev, node):
            if node in visitSet:
                return False

            visitSet.add(node)
            for c in adjL[node]:
                if c != prev and not dfs(node, c):
                    return False
            return True
        return (dfs(-1, 0)) and len(visitSet) == n
            
        