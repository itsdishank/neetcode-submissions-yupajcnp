class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjL =  defaultdict(list)
        for i, j in edges:
            if i != j:
                adjL[i].append(j)
                adjL[j].append(i)
            else:
                return False
        print(len(adjL), len(edges))
        if n != len(edges)+1:
            return False

        visitSet = []
        print(adjL)

        def dfs(prev, node):
            if node in visitSet:
                return False

            visitSet.append(node)
            for c in adjL[node]:
                print(node, c)
                if c != prev and not dfs(node, c):
                    return False
            return True
        #  (node not in adjL[c] and c in visitSet) and
        (dfs(None, 0))
        print(visitSet)
        return len(visitSet) == len(adjL)
            
        