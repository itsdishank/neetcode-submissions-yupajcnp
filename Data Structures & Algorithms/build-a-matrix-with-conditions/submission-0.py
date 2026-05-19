class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        empty = [[0]*k for _ in range(k)]
        rowG = defaultdict(list)
        for s, d in rowConditions:
            rowG[d].append(s)
        
        colG = defaultdict(list)
        for s, d in colConditions:
            colG[d].append(s)

        

        def dfs(node, g, res):
            if node in seen:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            for nei in g[node]:
                if not dfs(nei, g, res):
                    return False
            seen.add(node)
            res.append(node)
            visit.remove(node)
            return True

        visit = set()
        seen = set()
        resR = []
        for i in range(1, k+1):
            # if i in rowG:
            if not dfs(i, rowG, resR):
                return []
        
        
        visit = set()
        seen = set()
        resC = []
        for i in range(1, k+1):
            # if i in rowG:
            if not dfs(i, colG, resC):
                return []
        
        # print(resR)
        # print(resC)
        # print(colG, rowG)

        ind = {}

        for i in range(k):
            ind[resR[i]] = [i]
        for i in range(k):
            ind[resC[i]].append(i)
        
        # print(ind)

        for i in range(1, k+1):
            r, c = ind[i]
            empty[r][c] = i
        
        return empty




